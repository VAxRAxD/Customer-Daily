var main_state={
    'category':[],
    'count':[]
}
var main_data_url=`/api/sales_report/`
$.ajax({
    method:"GET",
    url:main_data_url,
    success:function(response){
        for (var i in response){
            var key=Object.keys(response[i])[0]
            var value=Object.values(response[i])[0]
            main_state.category.push(key)
            main_state.count.push(value)
            build()
        }
    }
});

function build(){
    var main_chartData = {
        type: "pie",
        plot: {
          backgroundColor : "#EAEAEA",
          size: 120,
          valueBox: {
            placement: 'out',
            text: '%t\n%npv%',
            fontFamily: "Open Sans"
          },
          tooltip: {
            fontSize: '10',
            fontFamily: "Open Sans",
            padding: "5 10",
            text: "%npv%"
          },
          animation: {
            effect: 2,
            method: 5,
            speed: 900,
            sequence: 1,
            delay: 10
          }
        },
        title: {
          fontColor: "#ffffff",
          text: 'Total product sold in past 30 days',
          align: "left",
          offsetX: 0,
          fontFamily: "Open Sans",
          fontSize: 18,
          backgroundColor: "#252A34"
        },
        plotarea: {
          backgroundColor: "#EAEAEA",
          margin: "20 0 0 0"
        },
        series: [
            {
            values: [main_state.count[0]],
            text: main_state.category[0],
            backgroundColor: '#009DAE',

          },
          {
            values: [main_state.count[1]],
            text: main_state.category[1],
            backgroundColor: '#FF5151',

          },
          {
            values: [main_state.count[2]],
            text: main_state.category[2],
            backgroundColor: '#FFAB4C',
          },
    ]
};
zingchart.render({
    id:"myChart",
    data:main_chartData,
});
}

var chicken_state={
    'category':[],
    'count':[]
}
var chicken_data_url=`/api/chicken_sales_report/`
$.ajax({
    method:"GET",
    url:chicken_data_url,
    success:function(response){
        for (var i in response){
            var key=Object.keys(response[i])[0]
            var value=Object.values(response[i])[0]
            chicken_state.category.push(key)
            chicken_state.count.push(value)
            chicken_build()
        }
    }
});
function chicken_build(){
    var chicken_chartData = {
        type: "pie",
        plot: {
          backgroundColor : "#EAEAEA",
          size: 120,
          valueBox: {
            placement: 'out',
            text: '%t\n%npv%',
            fontFamily: "Open Sans"
          },
          tooltip: {
            fontSize: '10',
            fontFamily: "Open Sans",
            padding: "5 10",
            text: "%npv%"
          },
          animation: {
            effect: 2,
            method: 5,
            speed: 900,
            sequence: 1,
            delay: 10
          }
        },
        title: {
          fontColor: "#ffffff",
          text: 'Chicken product sold in past 30 days',
          align: "left",
          offsetX: 0,
          fontFamily: "Open Sans",
          fontSize: 18,
          backgroundColor: "#252A34"
        },
        plotarea: {
          backgroundColor: "#EAEAEA",
          margin: "20 0 0 0"
        },
        series: [
            {
            values: [chicken_state.count[1]],
            text: chicken_state.category[1],
            backgroundColor: '#009DAE',

          },
          {
            values: [chicken_state.count[5]],
            text: chicken_state.category[5],
            backgroundColor: '#FF5151',

          },
          {
            values: [chicken_state.count[2]],
            text: chicken_state.category[2],
            backgroundColor: '#FFAB4C',
          },
          {
            values: [chicken_state.count[3]],
            text: chicken_state.category[3],
            backgroundColor: '#C36839',

          },
          {
            values: [chicken_state.count[4]],
            text: chicken_state.category[4],
            backgroundColor: '#34BE82',
          },
          {
            values: [chicken_state.count[0]],
            text: chicken_state.category[0],
            backgroundColor: '#FD6F96',
          },
    ]
};
zingchart.render({
    id:"chickenChart",
    data:chicken_chartData,
});
}

var seafood_state={
    'category':[],
    'count':[]
}
var seafood_data_url=`/api/seafood_sales_report/`
$.ajax({
    method:"GET",
    url:seafood_data_url,
    success:function(response){
        for (var i in response){
            var key=Object.keys(response[i])[0]
            var value=Object.values(response[i])[0]
            seafood_state.category.push(key)
            seafood_state.count.push(value)
            seafood_build()
        }
    }
});
function seafood_build(){
    var seafood_chartData = {
        type: "pie",
        plot: {
          backgroundColor : "#EAEAEA",
          size: 120,
          valueBox: {
            placement: 'out',
            text: '%t\n%npv%',
            fontFamily: "Open Sans"
          },
          tooltip: {
            fontSize: '10',
            fontFamily: "Open Sans",
            padding: "5 10",
            text: "%npv%"
          },
          animation: {
            effect: 2,
            method: 5,
            speed: 900,
            sequence: 1,
            delay: 10
          }
        },
        title: {
          fontColor: "#ffffff",
          text: 'Seafood product sold in past 30 days',
          align: "left",
          offsetX: 0,
          fontFamily: "Open Sans",
          fontSize: 18,
          backgroundColor: "#252A34"
        },
        plotarea: {
          backgroundColor: "#EAEAEA",
          margin: "20 0 0 0"
        },
        series: [
            {
            values: [seafood_state.count[0]],
            text: seafood_state.category[0],
            backgroundColor: '#009DAE',

          },
          {
            values: [seafood_state.count[1]],
            text: seafood_state.category[1],
            backgroundColor: '#FD6F96',

          },
          {
            values: [seafood_state.count[2]],
            text: seafood_state.category[2],
            backgroundColor: '#FF5151',

          },
          {
            values: [seafood_state.count[3]],
            text: seafood_state.category[3],
            backgroundColor: '#FFAB4C',
          },
          {
            values: [seafood_state.count[4]],
            text: seafood_state.category[4],
            backgroundColor: '#C36839',

          },
          {
            values: [seafood_state.count[5]],
            text: seafood_state.category[5],
            backgroundColor: '#34BE82',
          },
    ]
};
zingchart.render({
    id:"seafoodChart",
    data:seafood_chartData,
});
}

var mutton_state={
    'category':[],
    'count':[]
}
var mutton_data_url=`/api/mutton_sales_report/`
$.ajax({
    method:"GET",
    url:mutton_data_url,
    success:function(response){
        for (var i in response){
            var key=Object.keys(response[i])[0]
            var value=Object.values(response[i])[0]
            mutton_state.category.push(key)
            mutton_state.count.push(value)
            mutton_build()
        }
    }
});
function mutton_build(){
    var mutton_chartData = {
        type: "pie",
        plot: {
          backgroundColor : "#EAEAEA",
          size: 120,
          valueBox: {
            placement: 'out',
            text: '%t\n%npv%',
            fontFamily: "Open Sans"
          },
          tooltip: {
            fontSize: '10',
            fontFamily: "Open Sans",
            padding: "5 10",
            text: "%npv%"
          },
          animation: {
            effect: 2,
            method: 5,
            speed: 900,
            sequence: 1,
            delay: 10
          }
        },
        title: {
          fontColor: "#ffffff",
          text: 'Mutton product sold in past 30 days',
          align: "left",
          offsetX: 0,
          fontFamily: "Open Sans",
          fontSize: 18,
          backgroundColor: "#252A34"
        },
        plotarea: {
          backgroundColor: "#EAEAEA",
          margin: "20 0 0 0"
        },
        series: [
            {
            values: [mutton_state.count[0]],
            text: mutton_state.category[0],
            backgroundColor: '#009DAE',

          },
          {
            values: [mutton_state.count[1]],
            text: mutton_state.category[1],
            backgroundColor: '#FF5151',

          },
          {
            values: [mutton_state.count[2]],
            text: mutton_state.category[2],
            backgroundColor: '#FFAB4C',
          },
          {
            values: [mutton_state.count[3]],
            text: mutton_state.category[3],
            backgroundColor: '#C36839',

          },
          {
            values: [mutton_state.count[4]],
            text: mutton_state.category[4],
            backgroundColor: '#34BE82',
          },
    ]
};
zingchart.render({
    id:"muttonChart",
    data:mutton_chartData,
});
}