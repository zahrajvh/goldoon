
// category select

const category = document.querySelectorAll('.category-title');

category.forEach(item => {

    item.addEventListener('click', function(){

        
        for (let n = 0; n < category.length; n++) {
            category[n].classList.remove('active');
        }
        
        var categoryId = item.getAttribute('data-id');
        
        var blog = document.getElementsByClassName('blog');
        for (var j = 0; j < blog.length; j++) {
            blog[j].style.display = 'none';
        }
        
        var relatedBlog = document.querySelectorAll('.blog[data-category-id="' + categoryId + '"]');
        for (var k = 0; k < relatedBlog.length; k++) {
            relatedBlog[k].style.display = 'flex';
        }
        if (categoryId == "0") {
            var blog = document.getElementsByClassName('blog');
            for (var j = 0; j < blog.length; j++) {
                blog[j].style.display = 'flex';
            }
        }

        item.classList.add('active');

    })
} )




// var categories = document.getElementsByClassName('category');

// category.forEach(item => {
    
//     item.addEventListener('click', function(){
//     })
// } )


// // برای هر دسته‌بندی، یک event listener برای رویداد 'click' اضافه می‌کنیم
// for (var i = 0; i < categories.length; i++) {
//     categories[i].addEventListener('click', function() {

//         // تمام محصولات را مخفی می‌کنیم
        

//         // فقط محصولات مرتبط با دسته‌بندی انتخاب شده را نمایش می‌دهیم
//         var relatedProducts = document.querySelectorAll('.product[data-category-id="' + categoryId + '"]');
//         for (var k = 0; k < relatedProducts.length; k++) {
//             relatedProducts[k].style.display = 'block';
//         }
//     });
// }