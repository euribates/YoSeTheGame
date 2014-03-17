load = function() {
    data = document.grid;
    jQuery.each(data, function (y, row) {
        jQuery.each(row, function (x, cell) {
            console.log('Checking', x, ',', y, 'cell', cell);
            if (cell == 'bomb') {
                var id_cell = '#cell-' + (x+1) + 'x' + (y+1);
                var cell = jQuery(id_cell);
                cell.addClass('lost');
                }
            });
        });
    }


jQuery(document).ready(function () {
    load();
    });
