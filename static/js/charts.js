function loadHR(data){


for(var i=0; i<data.length; i++) {
    data[i][0] *= 1000;
}


        $('#chart_HR').highcharts('StockChart', {


            rangeSelector : {
                selected : 1
            },

            title : {
                text : "Heart Rate"
            },
		xAxis: {
            type: 'datetime',
            tickInterval: 3600 * 1000,
        },
            series : [{
                name : 'HR',
                data : data,
		color: 'red',
                tooltip: {
                    valueDecimals: 2
                }
            }]
        });

}
function loadEDA(data){


for(var i=0; i<data.length; i++) {
    data[i][0] *= 1000;
}


        $('#chart_EDA').highcharts('StockChart', {


            rangeSelector : {
                selected : 1
            },

            title : {
                text : "EDA"
            },
		xAxis: {
            type: 'datetime',
            tickInterval: 3600 * 1000,
        },
            series : [{
                name : 'EDA',
                data : data,
		color: 'blue',
                tooltip: {
                    valueDecimals: 2
                }
            }]
        });

}

function loadTEMP(data){


for(var i=0; i<data.length; i++) {
    data[i][0] *= 1000;
}


        $('#chart_TEMP').highcharts('StockChart', {


            rangeSelector : {
                selected : 1
            },

            title : {
                text : "Body temperature"
            },
		xAxis: {
            type: 'datetime',
            tickInterval: 3600 * 1000,
        },
            series : [{
                name : 'Body temperature',
                data : data,
		color: 'orange',
                tooltip: {
                    valueDecimals: 2
                }
            }]
        });

}
