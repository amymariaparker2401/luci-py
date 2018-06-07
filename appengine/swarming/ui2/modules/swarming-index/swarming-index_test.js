// Copyright 2018 The LUCI Authors. All rights reserved.
// Use of this source code is governed under the Apache License, Version 2.0
// that can be found in the LICENSE file.

import './index.js'

const fetchMock = require('fetch-mock');

beforeEach(function(){
  fetchMock.sandbox();

  // These are the default responses to the expected API calls (aka 'matched').
  // They can be overridden for specific tests, if needed.
  fetchMock.get('/_ah/api/swarming/v1/server/details', {
    server_version: '1234-abcdefg',
    bot_version: 'abcdoeraymeyouandme',
  });


  fetchMock.get('/_ah/api/swarming/v1/server/permissions', {
    get_bootstrap_token: false
  });

  fetchMock.post('/_ah/api/swarming/v1/server/token', 403);

  // Everything else
  fetchMock.catch(404);
});

afterEach(function() {
  // Completely remove the mocking which allows each test
  // to be able to mess with the mocked routes w/o impacting other tests.
  fetchMock.restore();
});

let container = document.createElement('div');
document.body.appendChild(container);

afterEach(function() {
  container.innerHTML = '';
});

// calls the test callback with one element 'ele', a created
// <swarming-index>.
// We can't put the describes inside the whenDefined callback because
// that doesn't work on Firefox (and possibly other places).
function createElement(test) {
  return window.customElements.whenDefined('swarming-index').then(() => {
    container.innerHTML = `<swarming-index client_id=for_test testing_offline=true></swarming-index>`;
    test(container.firstElementChild);
  });
}

function userLogsIn(ele, callback) {
  // The swarming-app emits the 'busy-end' event when all pending
  // fetches (and renders) have resolved.
  ele.addEventListener('busy-end', (e) => {
    callback();
  });
  let login = ele.querySelector('oauth-login');
  login._logIn();
  fetchMock.flush();
}

function becomeAdmin() {
  fetchMock.get('/_ah/api/swarming/v1/server/permissions', {
    get_bootstrap_token: true
  }, { overwriteRoutes: true });
  fetchMock.post('/_ah/api/swarming/v1/server/token', {
    bootstrap_token: '8675309JennyDontChangeYourNumber8675309'
  }, { overwriteRoutes: true });
}

describe('swarming-index', function() {

  describe('html structure', function() {
    it('contains swarming-app as its only child', function(done) {
      createElement((ele) => {
        expect(ele.children.length).toBe(1);
        expect(ele.children[0].tagName).toBe('swarming-app'.toUpperCase());
        done();
      });
    });

    describe('when not logged in', function() {
      it('tells the user they should log in', function(done){
        createElement((ele) => {
          let serverVersion = ele.querySelector('swarming-app>main .server_version');
          expect(serverVersion).toBeTruthy();
          expect(serverVersion.innerText).toContain('must log in');
          done();
        })
      })
      it('does not display the bootstrapping section', function(done){
        createElement((ele) => {
          let sectionHeaders = ele.querySelectorAll('swarming-app>main h2');
          expect(sectionHeaders).toBeTruthy();
          expect(sectionHeaders.length).toBe(2);
          done();
        })
      });
    });

    describe('when logged in as user (no bootstrap_token)', function() {
      it('displays the server version', function(done){
        createElement((ele) => {
          userLogsIn(ele, () => {
            let serverVersion = ele.querySelector('swarming-app>main .server_version');
            expect(serverVersion).toBeTruthy();
            expect(serverVersion.innerText).toContain('1234-abcdefg');
            done();
          });
        });
      });
      it('does not displays the bootstrapping section', function(done){
        createElement((ele) => {
          userLogsIn(ele, () => {
            let sectionHeaders = ele.querySelectorAll('swarming-app>main h2');
            expect(sectionHeaders).toBeTruthy();
            expect(sectionHeaders.length).toBe(2);
            done();
          });
        });
      });
      it('does not display the bootstrap token', function(done){
        createElement((ele) => {
          userLogsIn(ele, () => {
            let commandBox = ele.querySelector('swarming-app>main .command');
            expect(commandBox).toBeNull();
            done();
          });
        });
      });
    });

    describe('when logged in as admin (boostrap_token)', function() {
      beforeEach(becomeAdmin);

      it('displays the server version', function(done){
        createElement((ele) => {
          userLogsIn(ele, () => {
            let serverVersion = ele.querySelector('swarming-app>main .server_version');
            expect(serverVersion).toBeTruthy();
            expect(serverVersion.innerText).toContain('1234-abcdefg');
            done();
          });
        });
      });
      it('displays the bootstrapping section', function(done){
        createElement((ele) => {
          userLogsIn(ele, () => {
            let sectionHeaders = ele.querySelectorAll('swarming-app>main h2');
            expect(sectionHeaders).toBeTruthy();
            expect(sectionHeaders.length).toBe(3);
            done();
          });
        });
      });
      it('displays the bootstrap token', function(done){
        createElement((ele) => {
          userLogsIn(ele, () => {
            // There are several of these, but we'll just check one of them.
            let commandBox = ele.querySelector('swarming-app>main .command');
            expect(commandBox).toBeTruthy();
            expect(commandBox.innerText).toContain('8675309');
            done();
          });
        });
      });
    });
  }); // end describe('html structure')

  describe('api calls', function() {
    function expectNoUnmatchedCalls() {
      let calls = fetchMock.calls(false, 'GET');
      expect(calls.length).toBe(0);
      calls = fetchMock.calls(false, 'POST');
      expect(calls.length).toBe(0);
    }

    it('makes no API calls when not logged in', function(done){
      createElement((ele) => {
        fetchMock.flush().then(() => {
          // true in the first argument means 'matched calls',
          // that is calls that we expect and specified in the
          // beforeEach at the top of this file.
          let calls = fetchMock.calls(true, 'GET');
          expect(calls.length).toBe(0);
          calls = fetchMock.calls(true, 'POST');
          expect(calls.length).toBe(0);

          expectNoUnmatchedCalls();
          done();
        });
      });
    });

    it('makes authenticated API calls when a user logs in', function(done){
      createElement((ele) => {
        userLogsIn(ele, () => {
          let calls = fetchMock.calls(true, 'GET');
          expect(calls.length).toBe(2);
          // calls is an array of 2-length arrays with the first element
          // being the string of the url and the second element being
          // the options that were passed in
          let gets = calls.map((c) => c[0]);
          expect(gets).toContain('/_ah/api/swarming/v1/server/details');
          expect(gets).toContain('/_ah/api/swarming/v1/server/permissions');

          // check authorization headers are set
          calls.forEach((c) => {
            expect(c[1].headers).toBeDefined();
            expect(c[1].headers.authorization).toContain('Bearer ');
          })

          calls = fetchMock.calls(true, 'POST');
          expect(calls.length).toBe(0);

          expectNoUnmatchedCalls();
          done();
        });
      });
    });

    it('makes more authenticated API calls when an admin logs in', function(done){
      becomeAdmin();
      createElement((ele) => {
        userLogsIn(ele, () => {
          let calls = fetchMock.calls(true, 'GET');
          expect(calls.length).toBe(2);
          // calls is an array of 2-length arrays with the first element
          // being the string of the url and the second element being
          // the options that were passed in
          let gets = calls.map((c) => c[0]);
          expect(gets).toContain('/_ah/api/swarming/v1/server/details');
          expect(gets).toContain('/_ah/api/swarming/v1/server/permissions');

          // check authorization headers are set
          calls.forEach((c) => {
            expect(c[1].headers).toBeDefined();
            expect(c[1].headers.authorization).toContain('Bearer ');
          })

          calls = fetchMock.calls(true, 'POST');
          let posts = calls.map((c) => c[0]);
          expect(calls.length).toBe(1);
          expect(posts).toContain('/_ah/api/swarming/v1/server/token');

          // check authorization headers are set
          calls.forEach((c) => {
            expect(c[1].headers).toBeDefined();
            expect(c[1].headers.authorization).toContain('Bearer ');
          })

          expectNoUnmatchedCalls();
          done();
        });
      });
    });
  });
});