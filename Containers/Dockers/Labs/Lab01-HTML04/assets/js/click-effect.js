! function (i) {
    "use strict";
    i.fn.clickBubble = function (t) {
        var e = i.extend({
                color: "#674DD6",
                size: 20,
                time: 500,
                borderWidth: 2
            }, t),
            o = 0;
        return i(this).on("mousedown", function (t) {
            var r = t.clientX,
                n = i(window).scrollTop() + t.clientY;
            i("<div>").attr("id", "clickBubble_" + o++).css({
                width: 0,
                height: 0,
                border: e.borderWidth + "px solid " + e.color,
                position: "absolute",
                left: r,
                top: n,
                "border-radius": "50%"
            }).animate({
                width: e.size + "px",
                height: e.size + "px",
                left: r - .5 * e.size,
                top: n - .5 * e.size,
                opacity: 0
            }, e.time, function () {
                i(this).remove()
            }).appendTo("body")
        }), this
    }
}(jQuery);