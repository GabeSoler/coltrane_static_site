

$(function(){


//* Animations for cover index and brand

  $("#brand-text").velocity("headShake",{duration:1000});
  $("#landing-text").velocity("fadeInRight",{duration:600});
  $("#landing-button").velocity("fadeInRight",{duration:1000});
  $("#my_site_link").velocity("fadeInRight",{duration:1500});



//* Observer for cards
  
// define a callback function for the intersection observer. It receives an entry and a observer object that can stop observing    
  function animate_card_callback(entries,observer) {
    // entries are the observations
    entries.forEach(entry =>{
      //if an observation hits the options
      if (entry.isIntersecting){
        //trigger an animation
        entry.target.velocity("fadeInRight");
      }
    }
    )}
// define a set of options, in this case it gives a margin to the object or a threshold of visibility
  const card_observer_options = {
    rootMargin :"50px",
    //threshold : "0.1"
  }

  //define a observer object that receives a function and the options
  const card_observer = new IntersectionObserver(animate_card_callback, card_observer_options)

  //here I give each card an observer independently so each can trigger the function
  $(".card").not(":first").each(function (index,item){

    card_observer.observe($(item)[0]);
  }
  )


  //*Observer for first card's text

  // define a callback function for the intersection observer. It receives an entry and a observer object that can stop observing    
  function animate_text_callback(entries,observer) {
    entries.forEach(entry =>{
      if (entry.isIntersecting){
        entry.target.velocity("fadeInDownBig",
              {duration:2500}
            );
      }
    }
    )}


    const text_observer_options = {
      rootMargin :"-5px",
      //threshold : [0, 0.25, 0.5, 0.75, 1]
    }

  const text_observer = new IntersectionObserver(animate_text_callback, text_observer_options)

  text_observer.observe($("#animateText")[0]);
})
   