;(function($, window, undefined) {
    var didit = function(loadUrl) {
        this.loadUrl    = loadUrl;
        this.$container = $(document.getElementById('app-container'));
        this.$menu      = $(document.getElementById('app-menu'));

        this.$formTemplate = $(document.getElementById('form-template'));

        var that = this;
        this.$menu.on('click', '.list-item a', function(e) {
            e.preventDefault();

            that.select(this);
        });

        this.$menu.on('click', '.create-list a', function(e) {
            e.preventDefault();

            that.newList();
        })
    };

    didit.prototype.select = function(listItem) {
        this.$container.load($(listItem).attr('href'));
    };

    didit.prototype.newList = function() {
        var $content = $(this.$formTemplate.html());

        $content.find('textarea').markdown();

        $content.find('form').on('submit', function(e) {
            e.preventDefault();

            $.ajax({
                url: $(this).attr('action'),
                type: 'post',
                data: $(this).serialize(),
                success: function(response) {
                    window.location.reload(true);
                },
                error: console.log
           });
        });

        this.$container.html($content);
    };

    window.DiditApp = didit;
})(jQuery, this);