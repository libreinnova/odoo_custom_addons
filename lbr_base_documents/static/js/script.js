odoo.define('lbr_base_documents.image', function (require){
    "use strict";

    var fields = require('web.basic_fields');
    fields.FieldBinaryImage.include({
        events: _.extend({}, fields.FieldBinaryImage.prototype.events, {
            'click img': 'onImagePreview',
        }),
        onImagePreview: function () {
            // Nothing
        },
    });

});