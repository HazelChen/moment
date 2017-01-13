function add_word() {
    	var value = $('#add_word_input').val();

		jQuery.ajax({
			url: '/moment/add_word',
			data: JSON.stringify({'word': value}),
			type: 'POST',
			beforeSend: function(xhr, settings) {
        		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        			var csrftoken = getCookie('csrftoken');
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
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}