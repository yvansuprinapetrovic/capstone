document.addEventListener('DOMContentLoaded', function() {

    // Next question
    document.querySelector('#next').addEventListener('click', function(event) {
      
        console.log('Button clicked!')

        // getting the current question number using the this.dataset attribute
        const questionNumber = this.dataset.question;

        console.log(questionNumber)

        if (parseInt(questionNumber) === 10) {
          var x = "http://127.0.0.1:8000/quiz/summary";
          location.replace(y);

        } else {
          // converting it to an int and adding 1
          const num = parseInt(questionNumber) + 1;

          // composing new url to get next question
          var x = "http://127.0.0.1:8000/quiz/questions/";
          var y = x.concat(num);

          // using location.replace that disallows user to go back in history
          location.replace(y);
        }
        

    })

    // Multiple choice 
    document.querySelectorAll('.question').forEach(function(button) {
      button.onclick = function(event) {

        console.log('Button clicked!')
        
        // getting the value of the answer
        const choice = event.target;
        const answer = choice.getAttribute('value');
        console.log(answer)

        // if answer is correct
        if (answer == "True") {
          // show explanation with heading "correct"
          document.querySelector(`#explanation`).style.display = 'block';
          document.querySelector(`#correct`).innerHTML = "Correct";
          score();
        } else {
          // show explanation with heading "incorrect"
          document.querySelector(`#explanation`).style.display = 'block';
          document.querySelector(`#correct`).innerHTML = "Incorrect";
        }

        document.querySelector(`#next`).style.display = 'block';

      }
    })
  
  });


  // UPDATE SCORE
  function score() {

    // api call
    const score = 1;

    fetch('/quiz/score', {
      method: 'PUT',
      body: JSON.stringify({
        points: score
      }),
    })
    .then(result => {
        // Print result
        console.log(result);
    });

    return false;
  
  }