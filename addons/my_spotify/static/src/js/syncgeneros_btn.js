odoo.define('spotify.syncgeneros_btn', function(require){
    "use strict";

    let core           = require('web.core');
    let ListController = require("web.ListController");

    ListController.include({

        renderButtons: function($node){
            this._super.apply(this, arguments);
            if (this.$buttons){
                //console.debug("spotify.syncgeneros_btn: ", this.$buttons);
                this.$buttons.find('.o_syncgeneros_btn').click(this.proxy('action_def'));
            }
        },

        action_def : function(e){
            let self       = this;
            let active_id  = this.model.get(this.handle).getContext()['active_ids'];
            let model_name = this.model.get(this.handle).getContext()['active_model'];

            this._rpc({
                model: 'spotify.genero',
                method: 'sincronizar_generos',
                args: ["", model_name, active_id]
            });
        },


    });

});