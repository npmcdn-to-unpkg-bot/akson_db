        google.charts.load('current', {packages: ['corechart', 'table'], 'language': 'pl'});
        google.charts.setOnLoadCallback(drawDashboard);

        function drawDashboard() {
            //var users_data = {{users_data|safe}};
            var user_select = document.getElementById('user_select');
            var selected_user_index = -1;
            data_tables = {}
            data_tables_unique = {}
            /*users_data.forEach(function(user_data) {
                data_tables[user_data.user_id] = google.visualization.arrayToDataTable(user_data.data);
                data_tables_unique[user_data.user_id] = google.visualization.arrayToDataTable(user_data.unique);
            });*/

            function drawCharts(data_tables, chart, table, title_prefix = "") {
                var options = {
                    title: title_prefix + user_select.options[selected_user_index].text,
                    chartArea: {width: '70%', height: '80%'},
                    bar: {groupWidth: '100%'},
                    legend: {position: 'right'},
                    height: 400,
                    animation:{
                        startup: true,
                        duration: 500,
                        easing: 'out'
                    }
                };

                //var actual_data = data_tables[selected_user];
                chart.draw(data_tables, options);
                table.draw(data_tables, {});
            }

            var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
            var save_chart = document.getElementById('save_chart');
            var table = new google.visualization.Table(document.getElementById('table_div'));

            var chart_unique = new google.visualization.ColumnChart(document.getElementById('chart_unique_div'));
            var save_unique_chart = document.getElementById('save_unique_chart');
            var table_unique = new google.visualization.Table(document.getElementById('table_unique_div'));

            function drawAllCharts() {
                if (selected_user_index != user_select.selectedIndex) {
                    selected_user_index = user_select.selectedIndex;

                    var xmlhttp = new XMLHttpRequest();
                    var url = user_select.options[selected_user_index].value + "/";

                    xmlhttp.onreadystatechange = function() {
                    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                            var user_data = JSON.parse(xmlhttp.responseText);
                            console.log(user_data);
                            drawCharts(google.visualization.arrayToDataTable(user_data.data), chart, table, "Liczba wykonanych ćwiczeń dla osoby: ");
                            drawCharts(google.visualization.arrayToDataTable(user_data.unique), chart_unique, table_unique, "Liczba pacjentów dla osoby: ");
                        }
                    };
                    xmlhttp.open("GET", url, true);
                    xmlhttp.send();
                }
            }

            user_select.onkeyup = user_select.onchange = drawAllCharts;
            user_select.focus();
/*
            google.visualization.events.addListener(chart, 'ready', function () {
                save_chart.href = chart.getImageURI();
                save_chart.download = user_select.options[selected_user_index].text + ".png";
            });
            google.visualization.events.addListener(chart_unique, 'ready', function () {
                save_unique_chart.href = chart_unique.getImageURI();
                save_unique_chart.download = user_select.options[selected_user_index].text + ".png";
            });
*/
            drawAllCharts();
        }
