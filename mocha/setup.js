// JSDomGlobal provides no access to the JSDom API
(function globalJsdom() { // eslint-disable-line consistent-return
    const HTML = "<!doctype html><html><head><meta charset='utf-8'></head><body></body></html>"
    const keys = require("jsdom-global/keys") // eslint-disable-line global-require

    if (global.navigator &&
        global.navigator.userAgent &&
        global.navigator.userAgent.indexOf("Node.js") > -1 &&
        global.document &&
        typeof global.document.destroy === "function") {
        return global.document.destroy
    }

    const jsdom = require("jsdom") // eslint-disable-line global-require
    global.jsdom = new jsdom.JSDOM(HTML, {})
    global.document = global.jsdom.window.document
    global.window = global.jsdom.window
    global.window.console = global.console
    global.document.destroy = () => {
        keys.forEach(key => delete global[key])
    }

    keys.forEach(key => {
        global[key] = global.window[key]
    })
}())

// Noop function to make the tests pass
global.WebSocket = function () {} // eslint-disable-line func-names
global.Sinon = require("sinon").sandbox.create()
