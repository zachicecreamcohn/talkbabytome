function copyBabyIpsum() {
    var copyText = document.getElementById("babyipsum");
    copyText.select();
    navigator.clipboard.writeText(copyText.value).then(outFunc());

    // outFunc();

}

function outFunc() {
    document.querySelector("#copy_btn").textContent = "Copied!";
    setTimeout(()=> {document.querySelector("#copy_btn").textContent = "Copy";}, 2000);  // 1 second
}
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})