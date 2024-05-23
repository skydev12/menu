<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
    <!-- Add Prism.js CDN for syntax highlighting -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.27.0/themes/prism-okaidia.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        /* Customize your styles here */
        /* Example: */
        body {
            font-family: Arial, sans-serif;
        }
        .code-container {
            background-color: #000;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            position: relative; /* Add position relative for button placement */
            margin-top: 20px; /* Adjust margin top to match the card above */
        }
        .copy-button {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            font-size: 14px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        /* Add styles for like and comment buttons */
        .like-button {
            background-color: #3182ce;
            color: white;
            padding: 8px 16px;
            font-size: 14px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-right: 10px;
        }
        /* Add styles for like count */
        .like-count {
            color: #718096;
            font-size: 14px;
            margin-right: 20px;
        }
        /* ini untuk style menu */
        .card-container1 {
    background-color: #333; /* Warna hijau pekat */
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
}
        .icon-button {
        background: none;
        border: none;
        cursor: pointer;
        font-size: 3.2rem;
        margin: 10px;
        padding: 10px 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
        position: relative;
    }

    .icon-button:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.4);
    }

    /* Gaya Neon */
    .neon {
        color: #d8cdf1; /* Warna teks putih */
        text-shadow: 0 0 5px #00fff9, 0 0 10px #329e9c, 0 0 15px #00fff9, 0 0 20px #00fff9; /* Bayangan teks berwarna neon */
    }
/* ini end style menu */
    </style>
</head>
<body>
    <div x-data="setup()" x-init="$refs.loading.classList.add('hidden');">
    <div class="flex h-screen antialiased text-gray-900 bg-gray-100 dark:bg-dark dark:text-light">
      <!-- Loading screen -->
      <div
        x-ref="loading"
        class="fixed inset-0 z-50 flex items-center justify-center text-2xl font-semibold text-white bg-blue-600"
      >
        Loading.....
      </div>

      <!-- Sidebar -->
     <!-- Navigation Buttons -->
    <div class="card-container1">
        <div class="flex justify-center flex-wrap mt-5">
            <a href="index.html" class="icon-button neon">
                <i class="fas fa-home"></i>
            </a>
            <a href="kalku.html" class="icon-button neon">
                <i class="fas fa-calculator"></i>
            </a>
            <a href="kalender.html" class="icon-button neon">
                <i class="far fa-calendar-alt"></i>
            </a>
            <a href="solat.html" class="icon-button neon">
                <i class="fas fa-praying-hands"></i>
            </a>
            <a href="marketplace.html" class="icon-button neon">
                <i class="fas fa-shopping-cart"></i>
            </a>
            <a href="musik.html" class="icon-button neon">
                <i class="fas fa-music"></i>
            </a>
            <a href="elearning.html" class="icon-button neon">
                <i class="fas fa-book"></i>
            </a>
            <a href="alquran.html" class="icon-button neon">
                <i class="fas fa-quran"></i>
            </a>
            <a href="translate.html" class="icon-button neon">
                <i class="fas fa-language"></i>
            </a>
            <div class="bg-white shadow-md rounded p-4">
                <img src="10alpro.png" class="w-auto h-auto" alt="Image Description">
                <div class="text-sm text-gray-500 mb-4">
                    <h1>Ini adalah cuplikan tugas algoritma pemrograman pertemuan 10. Silahkan di-download file-nya pada tombol di bawah ini:</h1>
                    <!-- Add programming language column here -->
                    <div class="mt-4">
                        <h2 class="text-lg font-semibold">Programming Language:</h2>
                        <p>Python</p>
                    </div>
                </div>
                <a href="https://www.mediafire.com/file/lg64d1gwbmm9lyp/RISKY+DARLIS+23037035+ALPRO+11.pdf/file" download="file-name" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded text-lg">Download</a>
            </div>
            <div class="code-container code-container-2">
                <button class="copy-button" onclick="copyCode(1)">Salin</button>
                <div>
                    <button class="like-button" onclick="like(1)">Like</button>
                    <span class="like-count like-count-1">0 Like</span>
                </div>
                <pre><code id="code1" class="language-python">
                    =========================================================================================
                    ==================================INI ADALAH NO 1 A =====================================
                    =========================================================================================
                    
                    
                    import turtle
                    turtle.speed(5)  # Set kecepatan menjadi 5
                    
                    
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 B =====================================
                    =========================================================================================
                    
                    import turtle
                    turtle.penup()
                    turtle.goto(100, 100)  # Bergerak ke koordinat (100, 100) tanpa menggambar
                    
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 C =====================================
                    =========================================================================================
                    
                    import turtle
                    turtle.goto(50, 50)  # Bergerak ke koordinat (50, 50)
                    
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 D =====================================
                    =========================================================================================
                    
                    import turtle
                    turtle.circle(100)  # Menggambar lingkaran dengan jari-jari 100 unit
                    
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 E =====================================
                    =========================================================================================
                    
                    import turtle
                    turtle.color("red")  # Mengatur warna pen menjadi merah
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 B a ===================================
                    =========================================================================================
                    
                    import random
                    items = [1, 2, 3, 4, 5]
                    print(random.choice(items))  # Mengembalikan elemen acak dari list
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 B b ===================================
                    =========================================================================================
                    
                    import random
                    items = [1, 2, 3, 4, 5]
                    random.shuffle(items)
                    print(items)  # List items akan diacak
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 C a====================================
                    =========================================================================================
                    
                    from datetime import time
                    waktu = time(14, 30, 0)  # Membuat objek waktu 14:30:00
                    print(waktu)
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 C b====================================
                    =========================================================================================
                    
                    from datetime import datetime
                    sekarang = datetime.now()
                    print(sekarang.strftime("%Y-%m-%d %H:%M:%S"))  # Mengembalikan string tanggal dan waktu dalam format yang diberikan
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 D a====================================
                    =========================================================================================
                    
                    import math
                    print(math.factorial(5))  # Mengembalikan 120, karena 5! = 5 * 4 * 3 * 2 * 1
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 D b====================================
                    =========================================================================================
                    
                    import math
                    print(math.degrees(math.pi))  # Mengembalikan 180, karena π radian = 180 derajat
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 E a====================================
                    =========================================================================================
                    
                    import statistics
                    data = [1, 2, 3, 4, 5]
                    print(statistics.stdev(data))  # Mengembalikan standar deviasi sampel dari data
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 1 E b====================================
                    =========================================================================================
                    
                    import statistics
                    data = [1, 2, 3, 4, 5]
                    print(statistics.variance(data))  # Mengembalikan variansi sampel dari data
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 2 A======================================
                    =========================================================================================
                    
                    import pandas as pd
                    
                    # Membuat DataFrame dari dictionary
                    data = {
                        'Nama': ['A', 'B', 'C', 'D'],
                        'Umur': [23, 45, 25, 34],
                        'Kota': ['Jakarta', 'Bandung', 'Surabaya', 'Medan']
                    }
                    df = pd.DataFrame(data)
                    
                    # Menampilkan data
                    print("DataFrame:")
                    print(df)
                    
                    # Menghitung rata-rata umur
                    mean_umur = df['Umur'].mean()
                    print("\nRata-rata umur:", mean_umur)
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 2 B======================================
                    =========================================================================================
                    
                    import numpy as np
                    
                    # Membuat array numpy
                    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                    
                    # Menghitung rata-rata
                    mean = np.mean(data)
                    print("Rata-rata:", mean)
                    
                    # Menghitung standar deviasi
                    std_dev = np.std(data)
                    print("Standar Deviasi:", std_dev)
                    
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 2 C======================================
                    =========================================================================================
                    
                    import numpy as np
                    from scipy import stats
                    
                    # Data sampel
                    data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
                    
                    # Menghitung statistik deskriptif
                    mean = np.mean(data)
                    median = np.median(data)
                    mode_result = stats.mode(data, keepdims=True)  # Menggunakan keepdims=True untuk memastikan hasil dalam array 2D
                    variance = np.var(data)
                    std_dev = np.std(data)
                    
                    print("Mean:", mean)
                    print("Median:", median)
                    print("Mode:", mode_result.mode[0], "Frequency:", mode_result.count[0])
                    print("Variance:", variance)
                    print("Standard Deviation:", std_dev)
                    
                    =========================================================================================
                    ==================================INI ADALAH NO 3========================================
                    =========================================================================================
                    
                    import turtle
                    
                    # Setup screen
                    screen = turtle.Screen()
                    screen.title("Turtle Writing Example")
                    screen.bgcolor("white")
                    
                    # Create a turtle object
                    pen = turtle.Turtle()
                    pen.color("black")
                    pen.pensize(3)
                    
                    # Move the turtle to a starting position
                    pen.penup()
                    pen.goto(-100, 0)  # Adjust the position as needed
                    pen.pendown()
                    
                    # Write the text
                    pen.write("NANAD", font=("Arial", 24, "normal"))
                    
                    # Hide the turtle and display the window
                    pen.hideturtle()
                    turtle.done()
                     
                </code></pre>
            </div>
            
    </div>
        </div>
    </div>
    <!-- Add Prism.js CDN for syntax highlighting -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.27.0/prism.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.27.0/components/prism-python.min.js"></script>
    <script>
        function copyCode(num) {
            /* Get the text content of the code element */
            var codeElement = document.getElementById('code' + num);
            var codeText = codeElement.innerText;

            /* Create a textarea element to hold the code text */
            var textarea = document.createElement('textarea');
            textarea.value = codeText;

            /* Append the textarea to the document */
            document.body.appendChild(textarea);

            /* Select and copy the text from the textarea */
            textarea.select();
            document.execCommand('copy');

            /* Remove the textarea from the document */
            document.body.removeChild(textarea);

            /* Change button text to indicate success */
            var copyButton = document.querySelector('.copy-button');
            copyButton.textContent = 'Tersalin!';
            setTimeout(function() {
                copyButton.textContent = 'Salin';
            }, 2000); /* Change back to "Copy" after 2 seconds */
        }
        
        // Function to handle like button click
        function like(num) {
            var likeCount = localStorage.getItem('likeCount' + num);
            likeCount = likeCount ? parseInt(likeCount) + 1 : 1;
            localStorage.setItem('likeCount' + num, likeCount);
            updateLikeCount(likeCount, num);
        }
        // Function to update like count
        function updateLikeCount(count, num) {
            var likeCountElement = document.querySelector('.like-count-' + num);
            likeCountElement.textContent = count + ' Like';
        }
        // Initial update of like count
        for (var i = 1; i <= 1; i++) {
            updateLikeCount(localStorage.getItem('likeCount' + i) || 0, i);
        }
        
    </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/alpinejs/2.8.1/alpine.js"></script>
  <script>
      const setup = () => {
      return {
              isSidebarOpen: false,
          }
      }
  </script>
    <script>
        // Fungsi untuk kembali ke halaman sebelumnya
        function goBack() {
            window.history.back();
        }
    </script>
</body>
</html>
