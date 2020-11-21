
function sleep(waitMsec) {
  var startMsec = new Date();
  // loop unitl waitMsec
  while (new Date() - startMsec < waitMsec);
}

// require api and get plug info
const { Client } = require('tplink-smarthome-api')
const client = new Client();
const plug = client.getPlug({ host: '192.168.179.14' });

plug.setPowerState(true);
plug.setPowerState(false);
