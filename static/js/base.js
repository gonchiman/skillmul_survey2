const button = document.getElementById("menu-toggle");
const sidebar = document.getElementById("sidebar");

if (button && sidebar){
    button.addEventListener("click", function () {
        sidebar.classList.toggle("closed");
    });
}