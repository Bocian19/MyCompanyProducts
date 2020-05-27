document.addEventListener('DOMContentLoaded', function go() {

    $(function () {
        $('#logo').fadeIn(3000);
    });

    const visitsRows = document.querySelectorAll('.client_data');
    visitsRows.forEach(function start(visitRow) {

        const calendarDates = document.querySelectorAll('.fc-content-skeleton td');


            calendarDates.forEach(function showVisits(calendarDate) {
                if (calendarDate.dataset.date === visitRow.dataset.date) {
                    if (calendarDate.classList.contains('fc-fri')) {
                        const myCell = calendarDate.parentElement.parentElement.nextElementSibling.firstChild.childNodes[4];
                        myCell.innerHTML += visitRow.dataset.first_name + " " + visitRow.dataset.hour + "</br>";
                    } else if (calendarDate.classList.contains('fc-mon')) {
                        const myCell = calendarDate.parentElement.parentElement.nextElementSibling.firstChild.childNodes[0];
                        myCell.innerHTML += visitRow.dataset.first_name + " " + visitRow.dataset.hour + "</br>";
                    } else if (calendarDate.classList.contains('fc-tue')) {
                        const myCell = calendarDate.parentElement.parentElement.nextElementSibling.firstChild.childNodes[1];
                        myCell.innerHTML += visitRow.dataset.first_name + " " + visitRow.dataset.hour + "</br>";
                    } else if (calendarDate.classList.contains('fc-wed')) {
                        const myCell = calendarDate.parentElement.parentElement.nextElementSibling.firstChild.childNodes[2];
                        myCell.innerHTML += visitRow.dataset.first_name + " " + visitRow.dataset.hour + "</br>";
                    } else if (calendarDate.classList.contains('fc-thu')) {
                        const myCell = calendarDate.parentElement.parentElement.nextElementSibling.firstChild.childNodes[3];
                        myCell.innerHTML += visitRow.dataset.first_name + " " + visitRow.dataset.hour + "</br>";
                    }
                }
            });

    })
    const changeMonthButton = document.querySelectorAll('.fc-right button');

    changeMonthButton.forEach(button => {
        button.addEventListener('click', function () {
            go();
        })
    })

});

