 $(document).ready(function() {
  // Show validation message on material select dropdown
  $('select').material_select();
  $("select[required]").css({
      position: "absolute",
      display: "inline",
      height: 0,
      padding: 0,
      width: 0
  });




 });




