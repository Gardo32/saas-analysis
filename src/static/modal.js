document.addEventListener('DOMContentLoaded', (event) => {
    var plotModal = document.getElementById("plotModal");
    var heatmapModal = document.getElementById("heatmapModal");

    var plotBtn = document.getElementById("openPlotModalButton");
    var heatmapBtn = document.getElementById("openHeatmapModalButton");

    var span = document.getElementsByClassName("close");

    plotBtn.onclick = function () {
        plotModal.style.display = "block";
    }

    heatmapBtn.onclick = function () {
        heatmapModal.style.display = "block";
    }

    for (var i = 0; i < span.length; i++) {
        span[i].onclick = function () {
            plotModal.style.display = "none";
            heatmapModal.style.display = "none";
        }
    }

    window.onclick = function (event) {
        if (event.target == plotModal) {
            plotModal.style.display = "none";
        }
        if (event.target == heatmapModal) {
            heatmapModal.style.display = "none";
        }
    }
});
