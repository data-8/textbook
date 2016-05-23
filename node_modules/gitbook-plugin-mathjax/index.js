var Q = require('q');
var fs = require('fs');
var path = require('path');
var crc = require('crc');
var exec = require('child_process').exec;
var mjAPI = require('MathJax-node/lib/mj-single.js');

var started = false;
var countMath = 0;
var cache = {};

function convertTexToSvg(tex, options) {
    var d = Q.defer();
    options = options || {};

    if (!started) {
        mjAPI.config({MathJax: {SVG: {font: 'TeX'}}});
        mjAPI.start();
        started = true;
    }

    mjAPI.typeset({
        math: tex,
        format: (options.inline ? 'inline-TeX' : 'TeX'),
        svg: true,
        speakText: options.speakText || "default",
        speakRuleset: (options.speechrules || "mathspeak").replace(/^chromevox$/i, 'default'),
        speakStyle: options.speechstyle || "default",
        ex: options.ex || 6,
        width: options.width || 100,
        linebreaks: !!options.linebreaks
    }, function (data) {
        if (data.errors) return d.reject(new Error(data.errors));
        d.resolve(options.write? null : data.svg);
    });

    return d.promise;
}


module.exports = {
    book: {
        assets: "./book",
        js: [
            "https://cdn.mathjax.org/mathjax/2.5-latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML",
            "plugin.js"
        ]
    },
    blocks: {
        math: {
            shortcuts: {
                parsers: ["markdown", "asciidoc", "restructuredtext"],
                start: "$$",
                end: "$$"
            },
            process: function(blk) {
                var that = this;
                var tex = blk.body;
                var isInline = !(tex[0] == "\n");

                // For website return as script
                this.book.options.pluginsConfig.mathjax = this.book.options.pluginsConfig.mathjax || {};
                if ((this.book.options.generator == "website" || this.book.options.generator == "json")
                    && !this.book.options.pluginsConfig.mathjax.forceSVG) {
                    return '<script type="math/tex; '+(isInline? "": "mode=display")+'">'+blk.body+'</script>';
                }

                // Check if not already cached
                var hashTex = crc.crc32(tex).toString(16);

                // Return
                var imgFilename = "_mathjax_"+hashTex+".svg";
                var img = '<img src="/'+imgFilename+'" />';
                if (!isInline) {
                    img = '<div style="text-align:center;margin: 1em 0em;width: 100%;">'+img+'</div>';
                }

                return {
                    body: img,
                    post: function() {
                        if (cache[hashTex]) return;

                        cache[hashTex] = true;
                        countMath = countMath + 1;

                        return convertTexToSvg(tex, { inline: isInline })
                        .then(function(svg) {
                            return Q.nfcall(fs.writeFile, path.join(that.book.options.output, imgFilename), svg);
                        });
                    }
                };
            }
        }
    }
};
