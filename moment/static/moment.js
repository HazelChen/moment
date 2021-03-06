function add_word_post() {
    	var word = $('#add_word_input').val();
        var room = $('#room').val();

		jQuery.ajax({
			url: '/moment/add_word_public',
			data: JSON.stringify({'word': word, 'room': room}),
			type: 'POST',
			beforeSend: function(xhr, settings) {
        		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        			var csrftoken = getCookie('csrftoken') || $(":input[name='csrfmiddlewaretoken']").val();
            		xhr.setRequestHeader("X-CSRFToken", csrftoken);
        		}
    		},
			success: function() {
				location.reload();
			},
		});
	return false;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}