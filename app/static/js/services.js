const searchInput = document.getElementById("service-search");
const statusFilter = document.getElementById("service-filter");

const serviceRows = document.querySelectorAll(".service-row");


function filterServices() {

    const searchValue = searchInput.value.toLowerCase();
    const selectedStatus = statusFilter.value;

    serviceRows.forEach(function(row) {

        const serviceText = row.textContent.toLowerCase();
        const serviceStatus = row.dataset.status;

        const matchesSearch = serviceText.includes(searchValue);

        const matchesStatus =
            selectedStatus === "all" ||
            serviceStatus === selectedStatus;

        if (matchesSearch && matchesStatus) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }

    });

}


searchInput.addEventListener("input", filterServices);
statusFilter.addEventListener("change", filterServices);