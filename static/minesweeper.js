
load = function() {
    data = document.grid;
    jQuery.each(data, function (y, row) {
        jQuery.each(row, function (x, stat) {
            var id_cell = '#cell-' + (x+1) + 'x' + (y+1);
            var cell = jQuery(id_cell);
            if (stat == 'bomb') {
                cell.click(function (evt) {
                    var td = jQuery(evt.target);
                    td.addClass('lost');
                    });
                }
            });
        });
    }


jQuery(document).ready(function () {
    load();
    });
