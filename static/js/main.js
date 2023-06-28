
// TIMER IN TOAST IN CONTACT FORM AS THE TOAST IS IN BASE

var seconds = 0;

function updateTimer() {
    seconds += 5;

    var minutes = Math.floor(seconds / 60); // Calculate minutes
    var remainingSeconds = seconds % 60; // Calculate remaining seconds

    minutes = (minutes < 10 ? "0" : "") + minutes;
    remainingSeconds = (remainingSeconds < 10 ? "0" : "") + remainingSeconds;

    // Display the updated time
    if(remainingSeconds<60){
    document.getElementById("timer").innerHTML = remainingSeconds + 's ago';
    }
    if(remainingSeconds>=60){
    document.getElementById("timer").innerHTML = minutes + 'mins ago';
    }
}

setInterval(updateTimer, 5000);


// FORM HANDLING
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.row.g-3');

    form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent the default form submission

      // Get the form inputs
      const firstNameInput = document.querySelector('#firstName');
      const lastNameInput = document.querySelector('#lastName');
      const usernameInput = document.querySelector('#username');
      const emailInput = document.querySelector('#email');
      const password1Input = document.querySelector('#password1');
      const password2Input = document.querySelector('#password2');
      const termsCheckInput = document.querySelector('#gridCheck');

      // Perform input validation
      let isValid = true;

      if (firstNameInput.value.trim() === '') {
        firstNameInput.classList.add('is-invalid');
        isValid = false;
      } else {
        firstNameInput.classList.remove('is-invalid');
      }

      if (lastNameInput.value.trim() === '') {
        lastNameInput.classList.add('is-invalid');
        isValid = false;
      } else {
        lastNameInput.classList.remove('is-invalid');
      }

      if (usernameInput.value.trim() === '') {
        usernameInput.classList.add('is-invalid');
        isValid = false;
      } else {
        usernameInput.classList.remove('is-invalid');
      }

      if (emailInput.value.trim() === '' || !emailInput.checkValidity()) {
        emailInput.classList.add('is-invalid');
        isValid = false;
      } else {
        emailInput.classList.remove('is-invalid');
      }

      if (password1Input.value.trim() === '') {
        password1Input.classList.add('is-invalid');
        isValid = false;
      } else {
        password1Input.classList.remove('is-invalid');
      }

      if (password2Input.value.trim() === '' || password2Input.value !== password1Input.value) {
        password2Input.classList.add('is-invalid');
        isValid = false;
      } else {
        password2Input.classList.remove('is-invalid');
      }

      if (!termsCheckInput.checked) {
        termsCheckInput.classList.add('is-invalid');
        isValid = false;
      } else {
        termsCheckInput.classList.remove('is-invalid');
      }

      // Submit the form if all inputs are valid
      if (isValid) {
        form.submit();
      }
    });
  });