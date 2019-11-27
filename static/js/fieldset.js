/**
 * Created by Administrator on 2017/8/29.
 */
/*
    Easyui1.4.2
    Create time:2015-11-02  Author:duolaaqian

    $("#fs").lqfieldset({
        title:'个人信息',               //标题显示文字
        collapsible:true,               //是否可伸缩
        collapsed:false,                //初始化状态 是否为收起状态
        checkboxToggle:false,           //伸缩按钮是否为checkbox
        onBeforeCollapse:function(){    //收起之前调用该方法，返回false则取消收起
        },
        onCollapse:function(){          //收起之后调用该方法
        },
        onBeforeExpand:function(){      //展开之前调用该方法，返回false则取消展开
        },
        onExpand:function(){            //展开之后调用该方法
        }
    });

    $("#fs").lqfieldset('collapse');    //收起组件
    $("#fs").lqfieldset('expand');      //展开组件
*/
;(function ($) {
    //添加自定义方法
    function initFieldSet(thisObj){
        initDom(thisObj);
        refreshFront(thisObj);
    };
    function initDom(thisObj){
        var thisData = $.data(thisObj, "lqfieldset");
        var thisOptions = thisData.options;
        var innerDom = $(thisObj).wrap("<fieldset class='lq-fieldset'></fieldset>");
        innerDom.wrap('<div class="lq-fieldset-wrapmain" ></div>');
        innerDom = innerDom.parent('div.lq-fieldset-wrapmain');
        if(thisOptions.title||thisOptions.collapsible){
            var fieldSetDom = innerDom.parent('fieldset');
            thisOptions.fieldSetDom = fieldSetDom;
            var checkboxToggle = thisOptions.checkboxToggle;
            if(checkboxToggle){
                innerDom = innerDom.before("<legend class='lq-fieldset-legend'>"
                        +'<input type="checkbox" />'
                        +'<span>'+thisOptions.title+"</span></legend>");
                var dd = fieldSetDom.find('input[type=checkbox]');
                dd.unbind('.lqfieldset').bind('change.lqfieldset',function(){
                    var checked = $(this).prop("checked");
                    if(checked){
                        doExpand(thisObj);
                    }else{
                        doCollapse(thisObj);
                    }
                });
            }else{
                innerDom = innerDom.before("<legend class='lq-fieldset-legend'>"
                        +'<a href="javascript:void(0)" class="lq-fieldset-legend-icon"></a>'
                        +'<span>'+thisOptions.title+"</span></legend>");
                var dd = fieldSetDom.find('a.lq-fieldset-legend-icon');
                dd.unbind('.lqfieldset').bind('click.lqfieldset',function(){
                    var collapsed = thisOptions.collapsed;
                    if(collapsed){
                        doExpand(thisObj);
                    }else{
                        doCollapse(thisObj);
                    }
                }).bind('mouseover',function(){
                    dd.removeClass("mouseout").addClass("mouseover");
                }).bind('mouseout',function(){
                    dd.removeClass("mouseover").addClass("mouseout");
                });
            }
            if(!thisOptions.collapsible){
                fieldSetDom.find('.lq-fieldset-legend a').remove();
                fieldSetDom.find('.lq-fieldset-legend input[type=checkbox]').remove();
            }
        }
        diLimitSize(thisObj,innerDom);
    };
    function refreshFront(thisObj){
        var thisData = $.data(thisObj, "lqfieldset");
        var thisOptions = thisData.options;
        var collapsed = thisOptions.collapsed;
        if(collapsed){
            doCollapse(thisObj);
        }else{
            doExpand(thisObj);
        }
    };
    //收缩
    function doCollapse(thisObj){
        var thisData = $.data(thisObj, "lqfieldset");
        var thisOptions = thisData.options;
        if(thisOptions.onBeforeCollapse.call(thisObj) == false){
            return;
        }
        var fieldSetDom = thisOptions.fieldSetDom;
        thisOptions.collapsed = true;
        fieldSetDom.removeClass('expand').addClass('collapse');
        fieldSetDom.find('input[type=checkbox]').prop('checked',false);
        thisOptions.onCollapse.call(thisObj);
    };
    //展开
    function doExpand(thisObj){
        var thisData = $.data(thisObj, "lqfieldset");
        var thisOptions = thisData.options;
        if(thisOptions.onBeforeExpand.call(thisObj) == false){
            return;
        }
        var fieldSetDom = thisOptions.fieldSetDom;
        thisOptions.collapsed = false;
        fieldSetDom.removeClass('collapse').addClass('expand');
        fieldSetDom.find('input[type=checkbox]').prop('checked',true);
        thisOptions.onExpand.call(thisObj);
    };
    function diLimitSize(thisObj,innerDom){
        var thisData = $.data(thisObj, "lqfieldset");
        var thisOptions = thisData.options;
        var innerHeight = innerDom.height();
        var maxHeight = thisOptions.maxHeight;
        var minHeight = thisOptions.minHeight;
        if( maxHeight && $.isNumeric(maxHeight) ){
            if(innerHeight>maxHeight){
                innerDom.height(maxHeight);
            }
        }
        if( minHeight && $.isNumeric(minHeight) ){
            if(innerHeight<minHeight){
                innerDom.height(minHeight);
            }
        }
        var innerWidth = innerDom.width();
        var maxWidth = thisOptions.maxWidth;
        var minWidth = thisOptions.minWidth;
        if(maxWidth&&$.isNumeric(maxWidth)){
            if(innerWidth>maxWidth){
                innerDom.width(maxWidth);
            }
        }
        if(minWidth&&$.isNumeric(minWidth)){
            if(innerWidth<minWidth){
                innerDom.width(minWidth);
            }
        }
    };

    //初始化组件的时候调用此方法
    $.fn.lqfieldset = function(param1,param2){
        if (typeof param1 == "string") {
            return $.fn.lqfieldset.methods[param1](this, param2);
        }
        param1 = param1 || {};
        return this.each(function() {
            var thisData = $.data(this, "lqfieldset");
            if (thisData) {
                $.extend(thisData.options, param1);
            } else {
                thisData = $.data(this, "lqfieldset", {
                    options : $.extend( {}, $.fn.lqfieldset.defaults, param1)
                });
                initFieldSet(this);//自定义方法
            }
        });
    };
    //定义默认属性，初始化的时候可调用
    $.fn.lqfieldset.defaults = {
        title:"",
        maxHeight:null,
        collapsible: true,//是否可缩放
        collapsed: true,//初始状态是否缩放
        checkboxToggle: false,//缩放按钮是否显示为checkbox
        onBeforeCollapse:function(){
        },
        onCollapse:function(){
        },
        onBeforeExpand:function(){
        },
        onExpand:function(){
        }
    }
    //支持的方法
    $.fn.lqfieldset.methods = {
        lqfieldset:function(){
            alert("lqfieldset!");
        },
        options: function(thisObj) {
            var thisOptions = $.data(thisObj[0], "lqfieldset").options;
            return thisOptions;
        },
        collapse:function(thisObj){
            thisObj.each(function(){
                doCollapse(this);
            });
        },
        expand :function(thisObj){
            thisObj.each(function(){
                doExpand(this);
            });
        }
    }
})(jQuery);
