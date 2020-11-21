"use strict";

function sleep(waitMsec) {
  var startMsec = new Date(); // loop unitl waitMsec

  while (new Date() - startMsec < waitMsec) {
    ;
  }
} // require api and get plug info


var _require = require('tplink-smarthome-api'),
    Client = _require.Client;

var client = new Client();
var plug = client.getPlug({
  host: '192.168.179.14'
});
setTimeout(function () {
  plug.setPowerState(true);
}, 5000);
setTimeout(function () {
  plug.setPowerState(false);
}, 5000);