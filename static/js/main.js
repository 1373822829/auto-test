/**
 * Created by Administrator on 2017/7/18.
 */

var father = null
var current_selected = null
var basePath = 'http://localhost:8000/'


$(function(){
    //隐藏弹出窗口
    $('#w').window('close');
    $('#ww').window('close');
    $('#w1').window('close');
    $('#ww1').window('close');
    $('#dlg').dialog('close');
    $('#add').menubutton('disable')
    $('#edit').menubutton('disable')
    $('#remove').menubutton('disable')

    $('#loginOut').click(function () {
        $.messager.confirm('提示','您确定要退出本次登录吗？',function (r) {
            if(r){
                window.location.href="/login/"
            }
        })
    })
    // 获取选择菜单的父级菜单
    $('#tt').tree({
        onClick:function(data){
       //获取当前节点的父节点
        father = $(this).tree("getParent",data.target);
        current_selected = data;
        if (father!=null&&father.text == "用例管理"){
            $('#add').menubutton('enable')
            $('#edit').menubutton('enable')
            $('#remove').menubutton('enable')
        }else if (data.text == "用例管理"){
            $('#add').menubutton('enable')
            $('#edit').menubutton('disable')
            $('#remove').menubutton('disable')
        }else if(data.text == "用例执行"){
            $('#add').menubutton('enable')
            $('#edit').menubutton('disable')
            $('#remove').menubutton('disable')
        }else if(father!=null&&father.text=="用例执行"){
            $('#add').menubutton('disable')
            $('#edit').menubutton('enable')
            $('#remove').menubutton('enable')
        }else{
            $('#edit').menubutton('enable')
            $('#remove').menubutton('enable')
            $('#add').menubutton('disable')
        }
        var url = basePath + 'tabs/?name='+data.text+'&id='+data.id
        if($('#tt').tree('isLeaf',data.target)&&father.text!="用例管理"&&father.text!="用例执行"){
            if ($('#tab').tabs('exists', data.text)) {
                $('#tab').tabs('select', data.text);
            } else {
                var content = '<iframe scrolling="" frameborder="0"  src="' + url + '" style="width:100%;height:848px;"></iframe>';
                $('#tab').tabs('add', {
                    title: data.text,
                    content: content,
                    closable: true
                });
            }
        }
        if($('#tt').tree('isLeaf',data.target)&&father.text=="用例执行"){
            url = basePath+'tab/?name='+data.text+'&id='+data.id;
            if ($('#tab').tabs('exists', data.text)) {
                $('#tab').tabs('select', data.text);
            } else {
                var content = '<iframe scrolling="" frameborder="0"  src="' + url + '" style="width:100%;height:848px;"></iframe>';
                $('#tab').tabs('add', {
                    title: data.text,
                    content: content,
                    closable: true
                });
            }
        }
        }
    });
})


// 添加菜单
function addWorkstation() {
    if (current_selected.text == "用例管理"){
        var workstation = $('#workstation').combobox('getText');
        // addMenuCommon(workstation,"icon-folder");
        $.ajax({
                type : 'post',
                url : basePath+'add_workstation/',
                async : false,
                dataType : 'json',
                data : {'workstation':workstation},
                success: function (data) {
                    $.messager.show({
                        title: 'Success',
                        msg: data
                    })
                    $('#w').dialog('close')
                     location.reload()

                },
                error :function (data) {
                    $('#w').window('close');
                    $.messager.alert({title:'错误',msg:data.responseText,icon:'error',height:200})
                }
            });

    }else{
        $.messager.alert('警告','不能添加工作站!')
    }
}
// 删除菜单
function destroyMenu(){
    var node = $('#tt').tree('getSelected');
    if ($('#tt').tree('isLeaf',node.target)){
        if (node){

            $.messager.confirm('温馨提示','确定删除该菜单/用例?',function(r){
                if (r){
                            //刷新节点
                            var length = father.children.length;
                            var node = $("#tt").tree("getSelected");
                            var url = ''
                            if (father!=null&&father.text=="用例管理"){
                                url = basePath+'deleteWorkstation/';
                            }else{
                                url = basePath+'deleteTestCase/';
                            }
                            $.ajax({
                                type:'post',
                                url:url,
                                async:false,
                                dataType:'json',
                                data:{'id':node.id},
                                success:function (data) {
                                    $.messager.show({title: 'Success', msg: data});
                                    location.reload()

                                },
                                error:function (data) {
                                    $.messager.alert({title:'错误',msg:data.responseText,icon:'error',height:200})
                                }
                            })
                            if(length==1){
                                var className = $(father.target).children('span').eq(2).attr('class')+' icon-folder'
                                $(father.target).children('span').eq(2).attr('class',className)

                            }
                            //清空右侧表单数据
                            // $('#fm').form('clear');
                        }
            });
        }else{
             $.messager.show({
                title: 'Error',
                msg: "未选择要删除的菜单"
            });
        }
    }else{
        $.messager.alert('警告','请先删除节点下的子节点!')
    }
}
// 保存测试用例
function saveTestCase() {
    if (father!=null&&father.text == '用例管理'){
        // 获取测试用例名称
        var test_case = $('#test_case').val();
        $.ajax({
                type : 'post',
                url : basePath+'add_testcase/',
                async : false,
                dataType : 'json',
                data : {'testcase_name':test_case,'workstation':current_selected.text},
                success: function (data) {
                    if(data.status==0){
                        $.messager.alert('提示',data.data,'warning');
                    }else{$.messager.show({
                        title: 'Success',
                        msg: data.data
                    })
                        $('#w').dialog('close')
                        location.reload()
                        addMenuCommon(test_case,"")
                    }
                },
                error :function (data) {
                 $('#w').window('close');
                 $.messager.alert({title:'错误',msg:data.responseText,icon:'error',height:200})
                 }
            });
        var className = $($('#tt').tree('getSelected').target).children('span').eq(2).attr('class').replace(' icon-folder','')
        $($('#tt').tree('getSelected').target).children('span').eq(2).attr('class',className)
        $('#ww').window('close')
    }else if(current_selected.text=="用例执行"){
        // 获取测试用例名称
        var name = $('#test_case').val();
        $.ajax({
                type : 'post',
                url : basePath+'addCase/',
                async : false,
                dataType : 'json',
                data : {'name':name},
                success: function (data) {
                    if(data.status==0){
                        $.messager.alert('提示',data.message,'warning');
                    }else{$.messager.show({
                        title: 'Success',
                        msg: data.message
                    })
                        $('#w').dialog('close')
                        location.reload()
                    }
                },
                error :function (data) {
                 $('#w').window('close');
                 $.messager.alert({title:'错误',msg:data.responseText,icon:'error',height:200})
                 }
            });

    }else {
        $.messager.alert('警告','不能添加测试用例!')
    }

}
//添加菜单公共方法
function addMenuCommon(data,iconCls) {
   var node = $('#tt').tree('getSelected');
   if (node){
		var nodes = [{
			"id":1,
			"text":data,
            "iconCls":iconCls
		}];
		$('#tt').tree('append', {
			parent:node.target,
			data:nodes
		});
   }else{
         $.messager.show({
            title: 'Error',
            msg: "未选择要新增的菜单"
        });
        }
}

//修改工作站菜单
function updateWorkstation(){
    var text = $('#workstation1').combobox('getText')
    var node = $('#tt').tree('getSelected');
    $.ajax({
        type:'post',
        dataType : 'json',
        url:basePath+'updateWorkstation/',
        async:false,
        data:{'id':node.id,'workstation_name':text},
        success:function (data) {
            if(data.status) {
                $.messager.show({
                    title: 'Success',
                    msg: data.message
                })
                $('#w1').window('close');
                location.reload()
            }else {
                $('#w1').window('close');
                $.messager.alert('警告',data.message)
            }

        },
        error :function (data) {
            $('#w1').window('close');
            $.messager.alert({title:'错误',msg:data.responseText,icon:'error',height:200})
        }
    })


}
//修改用例菜单
function updateTestcase(){
    var text = $('#test_case1').val()
    var node = $('#tt').tree('getSelected');
     $.ajax({
        type:'post',
        dataType : 'json',
        url:basePath+'updateTestCase/',
        async:false,
        data:{'id':node.id,'testcase_name':text},
        success:function (data) {
            if(data.status) {
                $.messager.show({
                    title: 'Success',
                    msg: data.message
                })
                $('#ww1').window('close');
                location.reload()
            }else {
                $.messager.alert('提示',data.message,'warning')
            }
        },
        error :function (data) {
            $('#ww1').window('close');
            $.messager.alert({title:'错误',msg:data.responseText,icon:'error',height:200})
        }
    })

}




// 编辑
function updateMenu(){
    var menu_text = $('#tt').tree('getSelected').text
    if (father.text=="用例管理"){

            $('#w1').window('open');
            $('#workstation1').combobox('setText',menu_text)
            $('#workstation_save1').click(updateWorkstation)
    }else if(father.text=="用例执行"){

    }else{
            $('#ww1').window('open');
            $('#test_case1').val(menu_text)
            $('#testcase_save1').click(updateTestcase)
    }

}



// 处理CRSF令牌验证
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


