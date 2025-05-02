odoo.define('medicamento.widget', function (require) {
    "use strict";

    var fieldRegistry = require('web.field_registry');
    var AbstractField = require('web.AbstractField');

    var MedicamentoWidget = AbstractField.extend({
        template: 'MedicamentoWidgetTemplate',
        events: {
            'click .btn-toggle': '_onToggleClick',
        },

        _onToggleClick: function () {
            this._setValue(this.value === 'disponible' ? 'agotado' : 'disponible');
        },

        _render: function () {
            this.$el.html(`
                <button class="btn btn-primary btn-toggle">
                    ${this.value === 'disponible' ? '🟢 Disponible' : '🔴 Agotado'}
                </button>
            `);
        }
    });

    fieldRegistry.add('medicamento_widget', MedicamentoWidget);
});