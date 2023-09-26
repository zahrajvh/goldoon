const btn_filter = document.querySelector(".filter").querySelectorAll(".btn");
const flower = document.querySelectorAll(".flower-box");


btn_filter.forEach(btn => {
    btn.addEventListener("click", function () {
        
        if (btn.classList.contains("all")) {
            
            flower.forEach(item => {
                parent = item.parentNode
                grandParent = parent.parentNode
                grandParent.style.display = "block";
            });
            
        }

        else if (btn.classList.contains("apartment")) {
            
            flower.forEach(item => {
                if (item.classList.contains("apartment")) {
                    parent = item.parentNode
                    grandParent = parent.parentNode
                    grandParent.style.display = "block";
                }
                else {
                    parent = item.parentNode
                    grandParent = parent.parentNode
                    grandParent.style.display = "none";
                }
            });

        }

        else if (btn.classList.contains("garden")) {

            flower.forEach(item => {
                if (item.classList.contains("garden")) {
                    parent = item.parentNode
                    grandParent = parent.parentNode
                    grandParent.style.display = "block";
                }
                else {
                    parent = item.parentNode
                    grandParent = parent.parentNode
                    grandParent.style.display = "none";
                }
            });

        }

        else if (btn.classList.contains("ornamental")) {

            flower.forEach(item => {
                if (item.classList.contains("ornamental")) {
                    parent = item.parentNode
                    grandParent = parent.parentNode
                    grandParent.style.display = "block";
                }
                else {
                    parent = item.parentNode
                    grandParent = parent.parentNode
                    grandParent.style.display = "none";
                }
            });

        }
    })
});