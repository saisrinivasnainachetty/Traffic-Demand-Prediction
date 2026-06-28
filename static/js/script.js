// console.log("TrafficVision AI Loaded Successfully");
// ==============================
// Animated Counter
// ==============================

const counters = document.querySelectorAll(".counter");

const speed = 50;

const animateCounter = (counter)=>{

    const target = +counter.getAttribute("data-target");

    const update = ()=>{

        const value = +counter.innerText;

        const increment = target / speed;

        if(value < target){

            counter.innerText = (value + increment).toFixed(target % 1 !== 0 ? 1 : 0);

            requestAnimationFrame(update);

        }

        else{

            counter.innerText = target;

        }

    };

    update();

};

const observer = new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            animateCounter(entry.target);

            observer.unobserve(entry.target);

        }

    });

});

counters.forEach(counter=>{

    observer.observe(counter);

});