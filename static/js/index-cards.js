//for the cards in the index to have a nice entry

const items = document.querySelectorAll('.appear')

const active = function(entries){
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.classList.add('inview');
        }else{
            entry.target.classList.remove('inview');

        }
        });
    }

const io2 = new IntersectionObserver(active);
    for(let i=0; i< items.length; i++){
        io2.observe(items[i])
    }
