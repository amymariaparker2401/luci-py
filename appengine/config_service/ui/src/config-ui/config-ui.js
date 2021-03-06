/**
 * @license
 * Copyright 2020 The LUCI Authors. All rights reserved.
 * Use of this source code is governed under the Apache License, Version 2.0
 * that can be found in the LICENSE file.
 */

import "../common/auth-signin.js"
import "./config-set.js"
import "./front-page.js"

import { CommonBehavior } from "../common/common-behaviors.js"

import '@polymer/app-layout/app-drawer-layout/app-drawer-layout.js';
import '@polymer/app-layout/app-header/app-header.js';
import '@polymer/app-layout/app-header-layout/app-header-layout.js';
import '@polymer/app-layout/app-toolbar/app-toolbar.js';
import '@polymer/app-route/app-location.js';
import '@polymer/app-route/app-route.js';
import '@polymer/polymer/lib/elements/dom-if.js';

import { mixinBehaviors } from '@polymer/polymer/lib/legacy/class.js';
import { PolymerElement, html } from '@polymer/polymer/polymer-element.js';

class ConfigUI extends mixinBehaviors([CommonBehavior], PolymerElement) {
  static get template() {
    return html`
    <style>
      @media only screen and (min-width: 768px) {
        app-toolbar {
          height: 60px;
        }

        .logo {
          height: 50px;
        }

        .right { margin-left:15px; }
      }

      * { font-family: sans-serif; }

      app-toolbar {
        background-color: var(--google-blue-500);
        color: #232323;
      }

      .link {
        font-size: 75%;
        color: white;
        margin-right: 10px;
      }

      .title {
        text-decoration: none;
        color: white;
        font-size: 115%;
      }

      [main-title] {
        pointer-events: auto;
        margin-right: 100px;
      }

    </style>

    <app-drawer-layout fullbleed force-narrow>
      <app-header-layout>
        <app-header reveals slot="header">
          <app-toolbar>
            <!--<image class="logo" src="/static/images/chromium.png"/>-->
            <div main-title>
              <a href="/#/q/" class="title">
                Configuration Service
              </a>
            </div>

            <a href="/_ah/api/explorer"
              class="link"
              target="_blank">APIs explorer
            </a>

            <template is="dom-if" if="[[client_id]]">
              <auth-signin
                  class="right"
                  client_id="[[client_id]]"
                  auth_headers="{{auth_headers}}"
                  initialized="{{initialized}}"
                  profile="{{profile}}"
                  signed_in="{{signed_in}}">
              </auth-signin>
            </template>
            <template is="dom-if" if="[[_not(client_id)]]">
              <div class="right">No OAauth client id found.</div>
            </template>
          </app-toolbar>
        </app-header>

        <app-location route="{{route}}" use-hash-as-path></app-location>
        <app-route  route="{{route}}"
                    pattern="/services/:serviceName"
                    data="{{serviceData}}"
                    tail="{{serviceTail}}"
                    active="{{serviceActive}}"></app-route>

        <app-route  route="{{route}}"
                    pattern="/projects/:projectName"
                    data="{{projectData}}"
                    tail="{{projectTail}}"
                    active="{{projectActive}}"></app-route>

        <app-route  route="{{route}}"
                    pattern="/q/:query"
                    data="{{queryData}}"
                    active="{{frontPageActive}}"></app-route>

        <template is="dom-if" if="[[frontPageActive]]">
          <front-page auth_headers="[[auth_headers]]"
                      initialized="[[initialized]]"
                      signed_in="[[signed_in]]"
                      query="[[queryData.query]]"></front-page>
        </template>

        <template is="dom-if" if="[[serviceActive]]" restamp="true">
          <config-set category="services"
                      name="[[serviceData.serviceName]]"
                      route="[[serviceTail]]"
                      auth_headers="[[auth_headers]]"
                      initialized="[[initialized]]"
                      front-page-is-active="[[frontPageActive]]"
                      profile="[[profile]]"></config-set>
        </template>

        <template is="dom-if" if="[[projectActive]]" restamp="true">
          <config-set category="projects"
                      name="[[projectData.projectName]]"
                      route="[[projectTail]]"
                      auth_headers="[[auth_headers]]"
                      initialized="[[initialized]]"
                      front-page-is-active="[[frontPageActive]]"
                      profile="[[profile]]"></config-set>
        </template>
      </app-header-layout>
    </app-drawer-layout>
    `;
  }

  static get is() { return 'config-ui'; }

  static get properties() {
    return {
      client_id: {
        type: String,
        value: null
      },
      route: {
        type: Object,
        observer: '_routeChanged',
      }
    }
  }

  _routeChanged(route) {
    // If the path is blank, redirect to /q/
    if (!route.path || route.path == "/") {
      this.set('route.path', '/q/');
    }
  }

  ready() {
    super.ready();
    this._routeChanged(this.route);
  }
}

window.customElements.define(ConfigUI.is, ConfigUI);