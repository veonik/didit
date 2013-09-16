;(function($, window, undefined) {
    var didit = function(loadUrl) {
        _.extend(this, Backbone.Events);

        this.loadUrl    = loadUrl;
        this.$container = $(document.getElementById('app-container'));
        this.$menu      = $(document.getElementById('app-menu'));

        var that = this;
        this.$menu.on('click', 'a', function(e) {
            e.preventDefault();

            that.select($(this).data('id'));
        });
    };

    didit.prototype.select = function(id) {
        this.$container.load(this.loadUrl.replace('__', id));
    };

    window.DiditApp = didit;
})(jQuery, this);