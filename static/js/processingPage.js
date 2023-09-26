function showImage(event) {
    var input = event.target;
    var reader = new FileReader();
    reader.onload = function() {
      var img = document.getElementById("previewImage");
      img.src = reader.result;
      img.style.padding = "0"
    };
    reader.readAsDataURL(input.files[0]);
  }

  function checkFile() {
    // دریافت فایل انتخاب شده توسط کاربر
    var file = document.getElementById("fileInput").files[0];
 
    // بررسی اینکه فایل انتخاب شده است یا خیر
    if (!file) {
       // نمایش پیام خطا
       alert("لطفاً یک فایل را انتخاب نمایید.");
       return false;
    }
    return true;
 }