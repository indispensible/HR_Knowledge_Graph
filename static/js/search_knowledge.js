window.onload=function() {
    show_categories()
    search_knowledge()
    change_input()
}

var myChart = echarts.init(document.getElementById('show_graph'));
var myChart1 = echarts.init(document.getElementById('show_graph1'));
var myChart2 = echarts.init(document.getElementById('show_graph2'));
var entity

function show_categories() {
    // myChart.showLoading();
    $("#show_graph").show()
    $("#show_graph1").hide()
    $("#show_graph2").hide()

    option = {
        title: {
            text: '人力资源图谱'
        },
        tooltip: {},
        legend: {
            data:['销量']
        },
        xAxis: {
            data: ["IT","市场营销","人资/行政","财务/审计/法务","客服","航空"]
        },
        yAxis: {},
        series: [{
            name: '销量',
            type: 'bar',
            data: [858, 200, 164, 131, 18, 4]
        }]
    };
    myChart.setOption(option);
}

myChart.on('click', function(params){
        // alert(params.name + ":" + params.value)
        var category = params.name
        show_jobs(category)
})

function show_jobs(category) {
    // alert(category)
    $("#show_graph").hide()
    $("#show_graph1").show()
    $("#show_graph2").hide()

    var data = {'category': category}

    $.getJSON('/get_jobs/',data,function(res){
        // alert(res['twz'])
        graph(res, myChart1)
    })
}

myChart1.on('click',function(params){
        // alert("{'job':'" + params.name + "'}")
    var i = params.name
    if(i!="财务/审计/法务" && i!="客服" && i!="航空" && i!="市场营销" && i!="人资/行政" && i!="IT" && i!=entity){
        show_detail(i)
    }
})


function show_detail(job) {
    // alert(category)
    $("#show_graph").hide()
    $("#show_graph1").hide()
    $("#show_graph2").show()

    $("#job1").hide()
    $("#skill1").hide()
    $("#voacational1").hide()
    $("#professional1").hide()
    $("#industry1").hide()
    $("#function1").hide()
    $("#seniority1").hide()
    $("#qualification1").hide()
    $("#job_desc").hide()
    $("#job_req").hide()

    var data = {'title' : job.split('_')[0]}

    $.getJSON('/get_details_by_click/',data,function(res){
        // alert(res['twz'])
        graph(res, myChart2)
    })
}

// myChart2.on('click', function(params){
//     alert("成功")
// })

function update_repeat(data) {
    for(var i in data){
        for(var j in data){
            if(data[i] == data[j] && i != j){
                data[j] = data[j] + "_"
            }
        }
    }
    return data
}

function graph(jsontest, chart){
        jsontest = update_repeat(jsontest)
        $("#job1").hide()
        $("#skill1").hide()
        $("#voacational1").hide()
        $("#professional1").hide()
        $("#industry1").hide()
        $("#function1").hide()
        $("#seniority1").hide()
        $("#qualification1").hide()
        $("#job_desc").hide()
        $("#job_req").hide()

        $("#job").html("")
        $("#skill").html("")
        $("#voacational").html("")
        $("#professional").html("")
        $("#industry").html("")
        $("#function").html("")
        $("#seniority").html("")
        $("#qualification").html("")
        $("#job_desc1").html("")
        $("#job_req1").html("")

        var series_data_array = []

        var series_links_array = []

        entity = jsontest["entity"]

        var series_data = '{"name":"' + jsontest["entity"] +'","draggable": true}'

        var series_links = ''

        series_data = JSON.parse(series_data)

        series_data_array.push(series_data)

        var num = 0
        var length = 0
        var skill = 0
        var voacational = 0
        var qualification = 0
        var professional = 0
        var industry = 0
        var functions = 0
        var seniority = 0

        var key
        // chart.hideLoading()
        for(var i in jsontest){
            // alert(i + ":" + jsontest[i])
            if(i != "entity"){
                key = i.split("_")[0]
                if(key != "category"){
                    if(key == "job"){
                        length++
                        if(length >= 36){
                            break
                        }
                        num++
                        series_data = '{"name":"' + jsontest[i] +'","category": 1,"draggable": "true"}'
                        series_data = JSON.parse(series_data)
                        series_data_array.push(series_data)
                        series_links = '{"source": 0,"target":' +length+ ',"value":"岗位"}'
                        series_links = JSON.parse(series_links)
                        series_links_array.push(series_links)
                    }else if(key == "skill"){
                        skill++
                        if(skill >= 11){
                            continue
                        }
                        num++
                        var size = (parseInt(jsontest[i].split("#")[1]) - 1) * 2.5 + 50
                        series_data = '{"name":"' + jsontest[i] +'","category": 2,"draggable": "true","symbolSize":"'+size+'"}'
                        series_data = JSON.parse(series_data)
                        series_data_array.push(series_data)
                        series_links = '{"source": 0,"target":' +num+ ',"value":"技能"}'
                        series_links = JSON.parse(series_links)
                        series_links_array.push(series_links)
                    }else if(key == "voacational"){
                        voacational++
                        if(voacational >= 7){
                            continue
                        }
                        num++
                        var size = (parseInt(jsontest[i].split("#")[1]) - 1) * 2.5 + 50
                        series_data = '{"name":"' + jsontest[i] +'","category": 3,"draggable": "true","symbolSize":"'+size+'"}'
                        series_data = JSON.parse(series_data)
                        series_data_array.push(series_data)
                        series_links = '{"source": 0,"target":' +num+ ',"value":"业务"}'
                        series_links = JSON.parse(series_links)
                        series_links_array.push(series_links)
                    }else if(key == "qualification"){
                        qualification++
                        if(qualification >= 4){
                            continue
                        }
                        num++
                        var size = (parseInt(jsontest[i].split("#")[1]) - 1) * 2.5 + 50
                        series_data = '{"name":"' + jsontest[i] +'","category": 4,"draggable": "true","symbolSize":"'+size+'"}'
                        series_data = JSON.parse(series_data)
                        series_data_array.push(series_data)
                        series_links = '{"source": 0,"target":' +num+ ',"value":"学历要求"}'
                        series_links = JSON.parse(series_links)
                        series_links_array.push(series_links)
                    }else if(key == "professional"){
                        professional++
                        if(professional >= 6){
                            continue
                        }
                        num++
                        var size = (parseInt(jsontest[i].split("#")[1]) - 1) * 2.5 + 50
                        series_data = '{"name":"' + jsontest[i] +'","category": 5,"draggable": "true","symbolSize":"'+size+'"}'
                        series_data = JSON.parse(series_data)
                        series_data_array.push(series_data)
                        series_links = '{"source": 0,"target":' +num+ ',"value":"专业"}'
                        series_links = JSON.parse(series_links)
                        series_links_array.push(series_links)
                    }else if(key == "industry"){
                        industry++
                        if(industry >= 6){
                            continue
                        }
                        num++
                        var size = (parseInt(jsontest[i].split("#")[1]) - 1) * 2.5 + 50
                        series_data = '{"name":"' + jsontest[i] +'","category": 6,"draggable": "true","symbolSize":"'+size+'"}'
                        series_data = JSON.parse(series_data)
                        series_data_array.push(series_data)
                        series_links = '{"source": 0,"target":' +num+ ',"value":"行业"}'
                        series_links = JSON.parse(series_links)
                        series_links_array.push(series_links)
                    }else if(key == "function"){
                        functions++
                        if(functions >= 6){
                            continue
                        }
                        num++
                        var size = (parseInt(jsontest[i].split("#")[1]) - 1) * 2.5 + 50
                        series_data = '{"name":"' + jsontest[i] +'","category": 7,"draggable": "true","symbolSize":"'+size+'"}'
                        series_data = JSON.parse(series_data)
                        series_data_array.push(series_data)
                        series_links = '{"source": 0,"target":' +num+ ',"value":"职能"}'
                        series_links = JSON.parse(series_links)
                        series_links_array.push(series_links)
                    }else if(key == "seniority"){
                        seniority++
                        if(seniority >= 3){
                            continue
                        }
                        num++
                        var size = (parseInt(jsontest[i].split("#")[1]) - 1) * 2.5 + 50
                        series_data = '{"name":"' + jsontest[i] +'","category": 8,"draggable": "true","symbolSize":"'+size+'"}'
                        series_data = JSON.parse(series_data)
                        series_data_array.push(series_data)
                        series_links = '{"source": 0,"target":' +num+ ',"value":"年限"}'
                        series_links = JSON.parse(series_links)
                        series_links_array.push(series_links)
                    }else{
                        num = num
                    }
                }
            }
        }
        // alert(num)
        console.log(series_data_array)
        console.log(series_links_array)
        // for(var x in series_links_array){
        //     alert(x + ":" + series_links_array[x])
        // }

            // if(key == "job"){
            //     $("#job1").show()
            //     $("#job").append(number+':'+jsontest[j]+'&nbsp;&nbsp;&nbsp;')
            //     // $("#job").append(jsontest[j])
            // }else if(key == "skill"){
            //     $("#skill1").show()
            //     $("#skill").append(number+':'+jsontest[j]+'&nbsp;&nbsp;&nbsp;')
            // }

        // if(length >= 30){
            var j
            var number
            for(j in jsontest){
                if(j != "entity" && j != "req" && j != "desc") {
                    key = j.split("_")[0]
                    number = j.split("_")[1]
                    if (key == "job") {
                        $("#job1").show()
                        $("#job").append('<span id="'+ j +'" name="'+jsontest[j]+'" identity="job">'+number + ':' + jsontest[j] + '&nbsp;&nbsp;&nbsp;</span>')
                        // $("#job").append(jsontest[j])
                    } else if (key == "skill") {
                        $("#skill1").show()
                        $("#skill").append('<span id="'+ j +'" name="'+jsontest[j]+'" identity="skill">'+number + ':' + jsontest[j] + '&nbsp;&nbsp;&nbsp;</span>')
                    } else if (key == "voacational") {
                        $("#voacational1").show()
                        $("#voacational").append('<span id="'+ j +'" name="'+jsontest[j]+'" identity="vocational">'+number + ':' + jsontest[j] + '&nbsp;&nbsp;&nbsp;</span>')
                    } else if (key == "qualification") {
                        $("#qualification1").show()
                        $("#qualification").append('<span id="'+ j +'" name="'+jsontest[j]+'" identity="qualification">'+number + ':' + jsontest[j] + '&nbsp;&nbsp;&nbsp;</span>')
                    } else if (key == "professional") {
                        $("#professional1").show()
                        $("#professional").append('<span id="'+ j +'" name="'+jsontest[j]+'" identity="professional">'+number + ':' + jsontest[j] + '&nbsp;&nbsp;&nbsp;</span>')
                    } else if (key == "industry") {
                        $("#industry1").show()
                        $("#industry").append('<span id="'+ j +'" name="'+jsontest[j]+'" identity="industry">'+number + ':' + jsontest[j] + '&nbsp;&nbsp;&nbsp;</span>')
                    } else if (key == "function") {
                        $("#function1").show()
                        $("#function").append('<span id="'+ j +'" name="'+jsontest[j]+'" identity="function">'+number + ':' + jsontest[j] + '&nbsp;&nbsp;&nbsp;</span>')
                    } else if (key == "seniority") {
                        $("#seniority1").show()
                        $("#seniority").append('<span id="'+ j +'" name="'+jsontest[j]+'" identity="seniority">'+number + ':' + jsontest[j] + '&nbsp;&nbsp;&nbsp;</span>')
                    }
                // }
                }else if(j == "req"){
                        $("#job_req").show()
                        $("#job_req1").append(jsontest["req"])
                }else if(j == "desc"){
                        $("#job_desc").show()
                        $("#job_desc1").append(jsontest["desc"])
                }
            }
        // }

        chart.hideLoading()

        var option = {
            backgroundColor:'#f3f3f3',
            title: {
                text: '人力资源图谱'
            },
            tooltip: {},
            animationEasing: 'cubicInOut',
            animationDurationUpdate: 666,
            animationEasingUpdate: 'cubicInOut',
            label: {
                normal: {
                    show: true,
                    textStyle: {
                        fontSize: 12
                    },
                }
            },
            legend: {
                z: "center",
                show: false,
                data: ["entity", 'job', 'relation1', 'relation2', 'relation3', 'relation4', 'relation5', 'relation6', 'relation7']
            },
            series: [
                {
                    type: 'graph',
                    layout: 'force',
                    symbolSize: 66,
                    focusNodeAdjacency: true,
                    roam: true,
                    categories: [{
                        name: 'entity',
                        itemStyle: {
                            normal: {
                                color: "#009800",
                            }
                        }
                    }, {
                        name: 'job',
                        itemStyle: {
                            normal: {
                                color: "#4592FF",
                            }
                        }
                    }, {
                        name: 'relation1',
                        itemStyle: {
                            normal: {
                                color: "#CA8622",
                            }
                        }
                    }, {
                        name: 'relation2',
                        itemStyle: {
                            normal: {
                                color: "#C0C0C0",
                            }
                        }
                    }, {
                        name: 'relation3',
                        itemStyle: {
                            normal: {
                                color: "#BDA29A",
                            }
                        }
                    }, {
                        name: 'relation4',
                        itemStyle: {
                            normal: {
                                color: "#2F4554",
                            }
                        }
                    }, {
                        name: 'relation5',
                        itemStyle: {
                            normal: {
                                color: "#D48265",
                            }
                        }
                    }, {
                        name: 'relation6',
                        itemStyle: {
                            normal: {
                                color: "#91C7AE",
                            }
                        }
                    }, {
                        name: 'relation7',
                        itemStyle: {
                            normal: {
                                color: "#D48265",
                            }
                        }
                    }],
                    label: {
                        normal: {
                            show: true,
                            textStyle: {
                                fontSize: 12
                            },
                            align: 'center'
                        }
                    },
                    force: {
                        repulsion: 2333
                    },
                    edgeSymbolSize: [4, 50],
                    edgeLabel: {
                        normal: {
                            show: true,
                            textStyle: {
                                fontSize: 12
                            },
                            formatter: "{c}"
                        }
                    },
                    data: series_data_array,
                    links: series_links_array,
                    lineStyle: {
                        normal: {
                            opacity: 0.9,
                            width: 1,
                            curveness: 0
                        }
                    }
                }
            ]
        };
        chart.setOption(option);
        DNN_test()
}

function search_knowledge() {
    $("#search_something").click(function(){
        var detail = ""
        var jobs = ""
        detail = $("input[id='input_detail']").val();
        jobs = $("input[id='input_jobs']").val();
        if(detail != ""){
            // alert("第一个")
            $("#show_graph").hide()
            $("#show_graph1").hide()
            $("#show_graph2").show()

            $("#job1").hide()
            $("#skill1").hide()
            $("#voacational1").hide()
            $("#professional1").hide()
            $("#industry1").hide()
            $("#function1").hide()
            $("#seniority1").hide()
            $("#qualification1").hide()

            var data = {'title' : detail}

            myChart2.showLoading()
            $.getJSON('/get_details_by_search/',data,function(res){
                // alert(res['twz'])
                console.log(res)
                var length = 0
                for(var i in res){
                      length = length + 1
                }
                if(length == 1){
                    alert("未能检索到相关岗位详细信息")
                }else{
                    graph(res, myChart2)
                }
             })
        }else if(jobs != ""){
            // alert(jobs)
            $("#show_graph").hide()
            $("#show_graph1").show()
            $("#show_graph2").hide()

            if(jobs == "it" || jobs == "It" || jobs == "IT" || jobs == "iT" || jobs == "程序员"){
                jobs = "计算机"
            }

            var data = {'title' : jobs}

            myChart2.showLoading()
            $.getJSON('/find_type_potential_search/',data,function(res){
                // alert(res['twz'])
                console.log(res)
                var length = 0
                for(var i in res){
                      length = length + 1
                }
                if(length == 1){
                    alert("未能检索到相关岗位信息")
                }else{
                    graph(res, myChart1)
                }
             })
        }else{
            alert("输入框不能为空！")
        }
    })
}

var input_number = 0
function change_input() {
    $("#change").click(function(){
        input_number++
        if(input_number%2 == 1){
            $("#input_detail").val("")
            $("#input_jobs").val("")
            $("#input_detail").hide()
            $("#input_jobs").show()
        }else{
            $("#input_detail").val("")
            $("#input_jobs").val("")
            $("#input_detail").show()
            $("#input_jobs").hide()
        }
    })
}

function DNN_test() {
    $("span").click(function(e){
        var that = this
        var id = '#' + $(this).attr("id")
        // var title = $(this).attr("name").split('_')[0]
        // if (title == null || title == ""){
        //     title = $(that).attr("name").split("#")[0]
        // }
        var identity = $(this).attr("identity")

        var title
        if(identity == 'job'){
            title = $(this).attr("name").split('_')[0]
        }else{
            title = $(that).attr("name").split("#")[0]
        }

        if(identity == 'job'){
            if(confirm('是否要进一步查看"' + title + '"的细节？')){
                show_detail(title)
            }
        }else if(identity == "skill"){
            // alert(title)
            var patrn=/[\u4E00-\u9FA5]|[\uFE30-\uFFA0]/gi;
            var judge

            if(!patrn.exec(title)){
                judge = false;
            } else{
                judge = true;
            }

            data = {'title' : title}

            if (judge){
                if(/^[a-zA-Z]/.test(title)){
                    // alert("中英文")

                    // $.getJSON('/DNN_english/',data,function(res){
                    //     title = res['title']
                    //     layer.tips(title, id, {
                    //       tips: [1, '#3595CC'],
                    //       time: 4000
                    //     });
                    // })

                    title = "熟悉" + title
                    layer.tips(title, id, {
                      tips: [1, '#3595CC'],
                      time: 4000
                    });

                }else{
                    // alert("纯中文")
                    // $.getJSON('/DNN_chinese/',data,function(res){
                    //     title = res['title']
                    //     layer.tips(title, id, {
                    //       tips: [1, '#3595CC'],
                    //       time: 4000
                    //     });
                    // })
                    if(title.indexOf("能力") != -1){
                        title = "具备较强的" + title
                    }else{
                        title = "熟悉" + title
                    }
                    layer.tips(title, id, {
                      tips: [1, '#3595CC'],
                      time: 4000
                    });
                }
            }else{
                title = "熟悉" + title
                layer.tips(title, id, {
                  tips: [1, '#3595CC'],
                  time: 4000
                });
            }
        } else if(identity == "vocational"){
            title = "熟悉" + title
            layer.tips(title, id, {
              tips: [1, '#3595CC'],
              time: 4000
            });
        } else if(identity == "qualification"){
            title = "具备" + title + "及以上学历"
            layer.tips(title, id, {
              tips: [1, '#3595CC'],
              time: 4000
            });
        } else if(identity == "professional"){
            title = "毕业于" + title + "等相关专业者优先"
            layer.tips(title, id, {
              tips: [1, '#3595CC'],
              time: 4000
            });
        } else if(identity == "industry"){
            title = "有" + title + "等相关行业从业经验者优先"
            layer.tips(title, id, {
              tips: [1, '#3595CC'],
              time: 4000
            });
        } else if(identity == "function"){
            title = "主要职能为" + title
            layer.tips(title, id, {
              tips: [1, '#3595CC'],
              time: 4000
            });
        } else if(identity == "seniority"){
            title = "具备" + title + "以上从业经验者优先"
            layer.tips(title, id, {
              tips: [1, '#3595CC'],
              time: 4000
            });
        }
    })
}