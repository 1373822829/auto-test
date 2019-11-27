/**
 * Created by Administrator on 2017/7/18.
 */

function addTestCaseDetail() {
    $('#dlg').dialog('open')
    $.ajax({
      url: basePath+'load_workstation/',
      type : 'get',
      async : false,
      data: data,
      dataType: 'json',
      success: function (data) {
          alert(data)
          $('#cc').combobox('loadData',data['data']);
      }
    });
}
  //加载测试用例明细
function load_testcase_detail(object,testcase_id) {
     // 获取测试用例信息
    $.ajax({
        type : "post",
        url : basePath+'testcase_detail/',
        async : false,
        dataType : 'json',
        data : {'testcase_id':testcase_id},
        success : function (data) {
                            object.datagrid('loadData',data['data'])
        },
        error :function (data) {
            $.messager.alert({title:'错误',msg:data.responseText,icon:'error',height:200})
        }

    })

    }
//加载工作站下拉框
function loadWorkstationCombobox(id) {
    $.ajax({
          url: basePath+'load_workstation/',
          type : 'get',
          async : false,
          dataType: 'json',
          success: function (data) {
              $(id).combobox({
                  data:data['workstation'],
                  valueField:'id',
                  textField:'text',
              });
              },
          error :function (data) {
                $.messager.alert({title:'错误',msg:data.responseText,icon:'error',height:200})
            }
        });
}
//加载action下拉框
function loadActionCombobox(id) {
     $.ajax({
            type : 'get',
            url : basePath+'testcase_combobox/',
            async : false,
            dataType : 'json',
            success : function (data1) {
                $(id).combobox({
                    data:data1,
                    valueField:'id',
                    textField:'text',
                })
            },
            error :function (data) {
                $.messager.alert({title:'错误',msg:data.responseText,icon:'error',height:200})
            }

      })
}
