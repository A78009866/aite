document.addEventListener("DOMContentLoaded", function () {
    setTimeout(() => {
        document.querySelector(".profile-card").classList.remove("loading");
        document.querySelectorAll(".skeleton").forEach(el => el.classList.remove("skeleton"));
    }, 2000); // إزالة تأثير التحميل بعد ثانيتين
});
