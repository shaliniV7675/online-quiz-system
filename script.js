let time = 60;

const timerDisplay = document.getElementById('time');

const timer = setInterval(function () {
    time--;
    timerDisplay.textContent = time;

    if (time <= 0) {
        clearInterval(timer);
        alert('Time is up! Submitting your quiz.');
        document.getElementById('quizForm').submit();
    }
}, 1000);
