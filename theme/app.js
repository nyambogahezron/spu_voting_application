 document.getElementById('dropdownButton').onclick = function () {
        document.getElementById('dropdownContent').classList.toggle('show');
      };

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName('dropdown-content');
    for (var i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
};

function togglePasswordVisibility() {
          var passwordInput = document.getElementById('id_password');
          if (passwordInput.type === "password") {
              passwordInput.type = "text";
          } else {
              passwordInput.type = "password";
          }
      }
setTimeout(function() {
  var alert = document.getElementById('alert');
  if (alert) alert.style.display = 'none';
}, 3000);