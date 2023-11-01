window.onload = function () {
  $(function () {
    $('input#btn_translate').on('click', function () {
      const lang = $('input#language_code').val();
      console.log(lang);
      $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (data) {
        $('div#hello').html(data.hello);
      });
    });
  });
};
