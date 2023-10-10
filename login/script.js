function visible() {
    var x = document.getElementById("password");
    var y = document.getElementById("togglePassword");
    if (x.type === "password") {
      x.type = "text";
      y.className = "bi-eye-slash";
    } else {
      x.type = "password";
      y.className = "bi-eye";
    }
  }