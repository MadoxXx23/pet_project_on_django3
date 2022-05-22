const video = document.querySelector('.video'),
      playBtn = document.querySelector('.controls__play'),
      stopBtn = document.querySelector('.controls__stop'),
      platBtnImg = document.querySelector('.play__btn'),
      progress = document.querySelector('.progress'),
      time = document.querySelector('.controls__time')
      fullscreen = document.querySelector('.controls__fullscreen')


progress.value = 0

// Play & Pause video

function toggleVideoStatus() {
    if (video.paused) {
        video.play()
        platBtnImg.src = '/media/images/player/pause.png'
    } else {
        video.pause()
        platBtnImg.src = '/media/images/player/play.png'
    }
}


playBtn.addEventListener('click', toggleVideoStatus)
video.addEventListener('click', toggleVideoStatus)

// Stop video

function stopVideo() {
    video.currentTime = 0
    video.pause()
    platBtnImg.src = '/media/images/player/play.png'
}

stopBtn.addEventListener('click', stopVideo)


// Timer

function updateProgress() {
    
    progress.value = (video.currentTime / video.duration) * 100

    //Minutes

    let minutes = Math.floor(video.currentTime / 60)
    if (minutes < 10) {
        minutes = '0' + String(minutes)
    }

    //Secondes

    let seconds = Math.floor(video.currentTime % 60)
    if (seconds < 10) {
        seconds = '0' + String(seconds)
    }

    time.innerHTML = `${minutes}:${seconds}`

}

video.addEventListener('timeupdate', updateProgress)


// Set progress

function setProgress() {
    video.currentTime = (progress.value * video.duration) / 100
    // video.currentTime = "10.0"
    console.log(video.currentTime)
} 

progress.addEventListener('change', setProgress)


function openFullscreen() {
    if (video.requestFullscreen) {
        video.requestFullscreen();
    } else if (video.webkitRequestFullscreen) { /* Safari */
        video.webkitRequestFullscreen();
    } else if (video.msRequestFullscreen) { /* IE11 */
        video.msRequestFullscreen();
    }

    video.setAttribute('controls', "none")
}

function closeFullscreen() {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.webkitExitFullscreen) { /* Safari */
      document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { /* IE11 */
      document.msExitFullscreen();
    }
}


fullscreen.addEventListener('click', openFullscreen)



