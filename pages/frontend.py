home = """<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menga - Bosh Sahifa</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #2c3e50;
            --secondary: #3498db;
            --accent: #e74c3c;
            --light: #ecf0f1;
            --dark: #2c3e50;
            --text: #333;
            --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            line-height: 1.6;
            color: var(--text);
            background-color: #f9f9f9;
            overflow-x: hidden;
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header Styles */
        header {
            background-color: white;
            box-shadow: var(--shadow);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--primary);
            text-decoration: none;
            display: flex;
            align-items: center;
        }

        .logo i {
            margin-right: 10px;
            color: var(--secondary);
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--dark);
            font-weight: 500;
            transition: var(--transition);
            position: relative;
        }

        .nav-links a:hover {
            color: var(--secondary);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: -5px;
            left: 0;
            background-color: var(--secondary);
            transition: var(--transition);
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .auth-buttons {
            display: flex;
            gap: 1rem;
        }

        .btn {
            padding: 0.6rem 1.5rem;
            border-radius: 4px;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            border: none;
            font-size: 0.9rem;
        }

        .btn-outline {
            background: transparent;
            border: 1px solid var(--secondary);
            color: var(--secondary);
        }

        .btn-outline:hover {
            background: var(--secondary);
            color: white;
        }

        .btn-primary {
            background: var(--secondary);
            color: white;
        }

        .btn-primary:hover {
            background: var(--primary);
        }

        .mobile-menu {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
        }

        /* Hero Section */
        .hero {
            padding: 10rem 0 5rem;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 100" fill="%23ffffff" opacity="0.1"><polygon points="1000,0 1000,100 0,100"></polygon></svg>');
            background-size: cover;
        }

        .hero-content {
            max-width: 800px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }

        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }

        .hero-buttons {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 2rem;
        }

        .hero .btn {
            padding: 0.8rem 2rem;
            font-size: 1rem;
        }

        /* Features Section */
        .features {
            padding: 5rem 0;
            background: white;
        }

        .section-title {
            text-align: center;
            margin-bottom: 3rem;
        }

        .section-title h2 {
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 1rem;
        }

        .section-title p {
            color: #666;
            max-width: 600px;
            margin: 0 auto;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .feature-card {
            background: white;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: var(--shadow);
            transition: var(--transition);
            text-align: center;
        }

        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }

        .feature-icon {
            width: 70px;
            height: 70px;
            background: var(--light);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
            color: var(--secondary);
            font-size: 1.8rem;
        }

        .feature-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--primary);
        }

        /* CTA Section */
        .cta {
            padding: 5rem 0;
            background: linear-gradient(135deg, var(--secondary) 0%, var(--primary) 100%);
            color: white;
            text-align: center;
        }

        .cta h2 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
        }

        .cta p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
        }

        .cta .btn {
            background: white;
            color: var(--primary);
            font-size: 1.1rem;
            padding: 0.9rem 2.5rem;
        }

        .cta .btn:hover {
            background: var(--light);
        }

        /* Footer */
        footer {
            background: var(--dark);
            color: white;
            padding: 4rem 0 2rem;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .footer-column h3 {
            font-size: 1.3rem;
            margin-bottom: 1.5rem;
            position: relative;
            padding-bottom: 10px;
        }

        .footer-column h3::after {
            content: '';
            position: absolute;
            left: 0;
            bottom: 0;
            width: 40px;
            height: 2px;
            background: var(--secondary);
        }

        .footer-links {
            list-style: none;
        }

        .footer-links li {
            margin-bottom: 0.8rem;
        }

        .footer-links a {
            color: #bbb;
            text-decoration: none;
            transition: var(--transition);
        }

        .footer-links a:hover {
            color: white;
            padding-left: 5px;
        }

        .social-links {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
        }

        .social-links a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            color: white;
            transition: var(--transition);
        }

        .social-links a:hover {
            background: var(--secondary);
            transform: translateY(-3px);
        }

        .footer-bottom {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #bbb;
            font-size: 0.9rem;
        }

        /* Responsive Styles */
        @media (max-width: 992px) {
            .hero h1 {
                font-size: 2.8rem;
            }
        }

        @media (max-width: 768px) {
            .nav-links, .auth-buttons {
                display: none;
            }

            .mobile-menu {
                display: block;
            }

            .hero {
                padding: 8rem 0 4rem;
            }

            .hero h1 {
                font-size: 2.2rem;
            }

            .hero p {
                font-size: 1rem;
            }

            .hero-buttons {
                flex-direction: column;
                align-items: center;
            }

            .section-title h2 {
                font-size: 2rem;
            }
        }

        @media (max-width: 576px) {
            .hero h1 {
                font-size: 1.8rem;
            }

            .feature-card {
                padding: 1.5rem;
            }

            .cta h2 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <nav class="navbar">
                <a href="#" class="logo">
                    <i class="fas fa-rocket"></i>
                    Menga
                </a>
                <ul class="nav-links">
                    <li><a href="#">Bosh Sahifa</a></li>
                    <li><a href="#">Xizmatlar</a></li>
                    <li><a href="#">Loyihalar</a></li>
                    <li><a href="#">Jamoa</a></li>
                    <li><a href="#">Blog</a></li>
                    <li><a href="#">Aloqa</a></li>
                </ul>
                <div class="auth-buttons">
                    <button class="btn btn-outline">Kirish</button>
                    <button class="btn btn-primary">Ro'yxatdan o'tish</button>
                </div>
                <div class="mobile-menu">
                    <i class="fas fa-bars"></i>
                </div>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <h1>Kelajagingizni biz bilan quring</h1>
                <p>Menga - bu sizning biznesingizni rivojlantirish va raqamli dunyoda muvaffaqiyat qozonish uchun barcha vositalarni taqdim etuvchi platforma.</p>
                <div class="hero-buttons">
                    <button class="btn btn-primary">Boshlash</button>
                    <button class="btn btn-outline" style="background: rgba(255,255,255,0.2); color: white; border-color: white;">Ko'proq o'rganish</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="features">
        <div class="container">
            <div class="section-title">
                <h2>Bizning Xizmatlar</h2>
                <p>Biz sizga eng zamonaviy va samarali yechimlarni taklif etamiz</p>
            </div>
            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-laptop-code"></i>
                    </div>
                    <h3>Veb Dizayn</h3>
                    <p>Zamonaviy va foydalanuvchilar qulay bo'lgan veb-saytlar yaratamiz. Har bir loyiha individual yondashuv bilan ishlanadi.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-mobile-alt"></i>
                    </div>
                    <h3>Mobil Ilovalar</h3>
                    <p>iOS va Android platformalari uchun yuqori sifatli mobil ilovalar ishlab chiqamiz. Ilovalar tez va samarali ishlaydi.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <h3>Marketing</h3>
                    <p>Raqamli marketing strategiyalari orqali sizning biznesingizni rivojlantirishga yordam beramiz. Natijalar kafolatlangan.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta">
        <div class="container">
            <h2>Loyihangizni boshlashga tayyormisiz?</h2>
            <p>Biz bilan hamkorlik qiling va biznesingizni yangi bosqichga olib chiqing. Mutaxassislar jamoasi sizga yordam berishga tayyor.</p>
            <button class="btn">Bugun bog'laning</button>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-column">
                    <h3>Menga</h3>
                    <p>Biznesingizni rivojlantirish uchun barcha yechimlar. Biz bilan kelajagingizni quring.</p>
                    <div class="social-links">
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
                <div class="footer-column">
                    <h3>Xizmatlar</h3>
                    <ul class="footer-links">
                        <li><a href="#">Veb Dizayn</a></li>
                        <li><a href="#">Mobil Ilovalar</a></li>
                        <li><a href="#">Marketing</a></li>
                        <li><a href="#">SEO Optimizatsiya</a></li>
                        <li><a href="#">Branding</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3>Kompaniya</h3>
                    <ul class="footer-links">
                        <li><a href="#">Biz haqimizda</a></li>
                        <li><a href="#">Jamoa</a></li>
                        <li><a href="#">Karyera</a></li>
                        <li><a href="#">Blog</a></li>
                        <li><a href="#">Aloqa</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3>Aloqa</h3>
                    <ul class="footer-links">
                        <li><i class="fas fa-map-marker-alt"></i> Samarqand shahar.</li>
                        <li><i class="fas fa-phone"></i> +998 94 081 01 26</li>
                        <li><i class="fas fa-envelope"></i> smardonov203@gmail.com</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2023 Menga. Barcha huquqlar himoyalangan.</p>
            </div>
        </div>
    </footer>

    <script>
        // Mobile menu toggle
        document.querySelector('.mobile-menu').addEventListener('click', function() {
            const navLinks = document.querySelector('.nav-links');
            const authButtons = document.querySelector('.auth-buttons');
            
            navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
            authButtons.style.display = authButtons.style.display === 'flex' ? 'none' : 'flex';
            
            if (navLinks.style.display === 'flex') {
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '100%';
                navLinks.style.left = '0';
                navLinks.style.width = '100%';
                navLinks.style.background = 'white';
                navLinks.style.padding = '1rem 0';
                navLinks.style.boxShadow = '0 5px 10px rgba(0,0,0,0.1)';
                
                authButtons.style.position = 'absolute';
                authButtons.style.top = 'calc(100% + 180px)';
                authButtons.style.left = '0';
                authButtons.style.width = '100%';
                authButtons.style.justifyContent = 'center';
                authButtons.style.padding = '1rem 0';
                authButtons.style.background = 'white';
                authButtons.style.boxShadow = '0 5px 10px rgba(0,0,0,0.1)';
            } else {
                navLinks.style = '';
                authButtons.style = '';
            }
        });

        // Header background on scroll
        window.addEventListener('scroll', function() {
            const header = document.querySelector('header');
            if (window.scrollY > 50) {
                header.style.background = 'rgba(255, 255, 255, 0.95)';
                header.style.backdropFilter = 'blur(10px)';
            } else {
                header.style.background = 'white';
                header.style.backdropFilter = 'none';
            }
        });
    </script>
</body>
</html>"""


about = """<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shohjahon Mardonov | Haqimda</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #6C63FF;
            --secondary: #FF6584;
            --accent: #4ECDC4;
            --dark: #2A2D43;
            --light: #F7F9FC;
            --text: #333;
            --gradient-1: linear-gradient(135deg, #6C63FF 0%, #4ECDC4 100%);
            --gradient-2: linear-gradient(135deg, #FF6584 0%, #FCB564 100%);
            --gradient-3: linear-gradient(135deg, #A166FF 0%, #F76B1C 100%);
            --shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            --transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            line-height: 1.6;
            color: var(--text);
            background-color: var(--light);
            overflow-x: hidden;
        }

        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header Styles */
        header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            box-shadow: var(--shadow);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            transition: var(--transition);
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.2rem 0;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 800;
            color: var(--primary);
            text-decoration: none;
            display: flex;
            align-items: center;
            background: var(--gradient-1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .logo i {
            margin-right: 10px;
        }

        .nav-links {
            display: flex;
            list-style: none;
        }

        .nav-links li {
            margin-left: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--dark);
            font-weight: 600;
            transition: var(--transition);
            position: relative;
            padding: 5px 0;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 3px;
            bottom: 0;
            left: 0;
            background: var(--gradient-2);
            transition: var(--transition);
            border-radius: 10px;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .mobile-menu {
            display: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: var(--primary);
        }

        /* Hero Section */
        .about-hero {
            padding: 12rem 0 6rem;
            background: var(--gradient-1);
            color: white;
            position: relative;
            overflow: hidden;
        }

        .about-hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 100" fill="%23ffffff" opacity="0.1"><polygon points="1000,0 1000,100 0,100"></polygon></svg>');
            background-size: cover;
        }

        .hero-content {
            display: flex;
            align-items: center;
            gap: 4rem;
            position: relative;
            z-index: 1;
        }

        .hero-image {
            flex: 1;
            display: flex;
            justify-content: center;
        }

        .image-container {
            width: 300px;
            height: 300px;
            border-radius: 50%;
            overflow: hidden;
            border: 5px solid rgba(255, 255, 255, 0.3);
            box-shadow: var(--shadow);
            position: relative;
            background: var(--gradient-2);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .image-container::before {
            content: '';
            position: absolute;
            width: 320px;
            height: 320px;
            border-radius: 50%;
            background: conic-gradient(from 0deg, var(--primary), var(--secondary), var(--accent), var(--primary));
            animation: rotate 10s linear infinite;
            z-index: -1;
        }

        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .image-container img {
            width: 290px;
            height: 290px;
            border-radius: 50%;
            object-fit: cover;
            background: var(--light);
        }

        .hero-text {
            flex: 1;
        }

        .hero-text h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            line-height: 1.2;
        }

        .hero-text .title {
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            opacity: 0.9;
            font-weight: 500;
        }

        .hero-text p {
            font-size: 1.1rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }

        .social-links {
            display: flex;
            gap: 1rem;
        }

        .social-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.2);
            color: white;
            font-size: 1.3rem;
            transition: var(--transition);
            text-decoration: none;
        }

        .social-btn:hover {
            transform: translateY(-5px);
            background: white;
            color: var(--primary);
        }

        /* About Section */
        .about-section {
            padding: 6rem 0;
            background: white;
        }

        .section-title {
            text-align: center;
            margin-bottom: 4rem;
        }

        .section-title h2 {
            font-size: 2.8rem;
            background: var(--gradient-1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            display: inline-block;
        }

        .section-title p {
            color: #666;
            max-width: 600px;
            margin: 0 auto;
            font-size: 1.1rem;
        }

        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }

        .about-text h3 {
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            color: var(--dark);
        }

        .about-text p {
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
            color: #555;
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 2rem;
        }

        .skill-tag {
            padding: 0.6rem 1.2rem;
            background: var(--light);
            border-radius: 30px;
            font-weight: 600;
            color: var(--dark);
            transition: var(--transition);
            cursor: pointer;
            border: 2px solid transparent;
        }

        .skill-tag:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow);
            border-color: var(--primary);
        }

        .skill-tag:nth-child(2n) {
            background: var(--gradient-1);
            color: white;
        }

        .skill-tag:nth-child(3n) {
            background: var(--gradient-2);
            color: white;
        }

        .skill-tag:nth-child(4n) {
            background: var(--gradient-3);
            color: white;
        }

        /* Stats Section */
        .stats-section {
            padding: 5rem 0;
            background: var(--gradient-2);
            color: white;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
        }

        .stat-card {
            text-align: center;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            backdrop-filter: blur(10px);
            transition: var(--transition);
        }

        .stat-card:hover {
            transform: translateY(-10px);
            background: rgba(255, 255, 255, 0.2);
        }

        .stat-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
        }

        .stat-text {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        /* Projects Section */
        .projects-section {
            padding: 6rem 0;
            background: var(--light);
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .project-card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: var(--transition);
        }

        .project-card:hover {
            transform: translateY(-15px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }

        .project-image {
            height: 200px;
            background: var(--gradient-3);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 3rem;
        }

        .project-content {
            padding: 1.5rem;
        }

        .project-content h3 {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            color: var(--dark);
        }

        .project-content p {
            color: #666;
            margin-bottom: 1.5rem;
        }

        .project-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
        }

        .project-tag {
            padding: 0.3rem 0.8rem;
            background: var(--light);
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--dark);
        }

        .project-btn {
            display: inline-block;
            padding: 0.7rem 1.5rem;
            background: var(--primary);
            color: white;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
        }

        .project-btn:hover {
            background: var(--secondary);
            transform: translateY(-3px);
        }

        /* CTA Section */
        .cta-section {
            padding: 6rem 0;
            background: var(--gradient-3);
            color: white;
            text-align: center;
        }

        .cta-section h2 {
            font-size: 2.8rem;
            margin-bottom: 1.5rem;
        }

        .cta-section p {
            font-size: 1.2rem;
            margin-bottom: 2.5rem;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
            opacity: 0.9;
        }

        .cta-buttons {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            flex-wrap: wrap;
        }

        .btn {
            padding: 0.9rem 2.2rem;
            border-radius: 30px;
            font-weight: 700;
            cursor: pointer;
            transition: var(--transition);
            border: none;
            font-size: 1rem;
            text-decoration: none;
            display: inline-block;
        }

        .btn-primary {
            background: white;
            color: var(--dark);
        }

        .btn-primary:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }

        .btn-outline {
            background: transparent;
            border: 2px solid white;
            color: white;
        }

        .btn-outline:hover {
            background: white;
            color: var(--dark);
            transform: translateY(-5px);
        }

        /* Footer */
        footer {
            background: var(--dark);
            color: white;
            padding: 4rem 0 2rem;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .footer-column h3 {
            font-size: 1.3rem;
            margin-bottom: 1.5rem;
            position: relative;
            padding-bottom: 10px;
        }

        .footer-column h3::after {
            content: '';
            position: absolute;
            left: 0;
            bottom: 0;
            width: 40px;
            height: 2px;
            background: var(--secondary);
        }

        .footer-links {
            list-style: none;
        }

        .footer-links li {
            margin-bottom: 0.8rem;
        }

        .footer-links a {
            color: #bbb;
            text-decoration: none;
            transition: var(--transition);
        }

        .footer-links a:hover {
            color: white;
            padding-left: 5px;
        }

        .footer-social {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
        }

        .footer-social a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            color: white;
            transition: var(--transition);
        }

        .footer-social a:hover {
            background: var(--primary);
            transform: translateY(-3px);
        }

        .footer-bottom {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: #bbb;
            font-size: 0.9rem;
        }

        /* Responsive Styles */
        @media (max-width: 992px) {
            .hero-text h1 {
                font-size: 2.8rem;
            }
            
            .about-content {
                grid-template-columns: 1fr;
                gap: 3rem;
            }
        }

        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .mobile-menu {
                display: block;
            }

            .about-hero {
                padding: 10rem 0 4rem;
            }

            .hero-content {
                flex-direction: column;
                text-align: center;
                gap: 2rem;
            }

            .hero-text h1 {
                font-size: 2.2rem;
            }

            .section-title h2 {
                font-size: 2.2rem;
            }

            .cta-section h2 {
                font-size: 2.2rem;
            }
        }

        @media (max-width: 576px) {
            .hero-text h1 {
                font-size: 1.8rem;
            }

            .stat-number {
                font-size: 2.5rem;
            }

            .cta-section h2 {
                font-size: 1.8rem;
            }

            .cta-buttons {
                flex-direction: column;
                align-items: center;
            }

            .btn {
                width: 100%;
                max-width: 250px;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <nav class="navbar">
                <a href="#" class="logo">
                    <i class="fas fa-user-astronaut"></i>
                    Shohjahon
                </a>
                <ul class="nav-links">
                    <li><a href="#">Bosh Sahifa</a></li>
                    <li><a href="#about">Haqimda</a></li>
                    <li><a href="#skills">Ko'nikmalar</a></li>
                    <li><a href="#projects">Loyihalar</a></li>
                    <li><a href="#contact">Aloqa</a></li>
                </ul>
                <div class="mobile-menu">
                    <i class="fas fa-bars"></i>
                </div>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="about-hero">
        <div class="container">
            <div class="hero-content">
                <div class="hero-image">
                    <div class="image-container">
                        <!-- Placeholder for profile image -->
                        <div style="width: 290px; height: 290px; border-radius: 50%; background: var(--light); display: flex; align-items: center; justify-content: center; font-size: 5rem; color: var(--primary);">
                            <i class="fas fa-user"></i>
                        </div>
                    </div>
                </div>
                <div class="hero-text">
                    <h1>Shohjahon Mardonov</h1>
                    <div class="title">Full Stack Dasturchi & UI/UX Dizayner</div>
                    <p>Men frontend va backend texnologiyalari bo'yicha 5 yillik tajribaga ega dasturchiman. Zamonaviy va foydalanuvchilar qulay bo'lgan veb-ilovalar yaratishga ixtisoslashganman.</p>
                    <div class="social-links">
                        <a href="#" class="social-btn"><i class="fab fa-github"></i></a>
                        <a href="#" class="social-btn"><i class="fab fa-linkedin-in"></i></a>
                        <a href="#" class="social-btn"><i class="fab fa-telegram"></i></a>
                        <a href="#" class="social-btn"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about-section">
        <div class="container">
            <div class="section-title">
                <h2>Mening Haqimda</h2>
                <p>Men kimman va nima qilaman</p>
            </div>
            <div class="about-content">
                <div class="about-text">
                    <h3>Dasturlash - bu mening ishqim</h3>
                    <p>Men dasturlashni 2018-yilda boshlaganman va shu kungacha turli xil loyihalarda ishlab kelaman. Mening asosiy maqsadim - foydalanuvchilar uchun qulay va zamonaviy veb-ilovalar yaratish.</p>
                    <p>Men turli xil texnologiyalar va frameworklar bilan ishlashni yaxshi ko'raman. Har bir yangi loyiha - bu yangi imkoniyat va yangi tajriba.</p>
                    <p>Bo'sh vaqtimda men yangi texnologiyalarni o'rganishga, open source loyihalarga hissa qo'shishga va dasturlash hamjamiyatida faol ishtirok etishga harakat qilaman.</p>
                    
                    <div id="skills" class="skills">
                        <div class="skill-tag">HTML5</div>
                        <div class="skill-tag">CSS3</div>
                        <div class="skill-tag">JavaScript</div>
                        <div class="skill-tag">React</div>
                        <div class="skill-tag">Vue.js</div>
                        <div class="skill-tag">Node.js</div>
                        <div class="skill-tag">Python</div>
                        <div class="skill-tag">Django</div>
                        <div class="skill-tag">MongoDB</div>
                        <div class="skill-tag">PostgreSQL</div>
                        <div class="skill-tag">Git</div>
                        <div class="skill-tag">Docker</div>
                    </div>
                </div>
                <div class="about-text">
                    <h3>Tajribam</h3>
                    <p>Men turli xil kompaniyalarda va frilans sifatida ishlaganman. Mening eng muhim loyihalarim orasida:</p>
                    <ul style="list-style-type: none; margin-top: 1rem;">
                        <li style="padding: 0.5rem 0; border-bottom: 1px solid #eee;">
                            <strong>E-commerse platformasi</strong> - React va Node.js asosida
                        </li>
                        <li style="padding: 0.5rem 0; border-bottom: 1px solid #eee;">
                            <strong>CRM tizimi</strong> - Vue.js va Django asosida
                        </li>
                        <li style="padding: 0.5rem 0; border-bottom: 1px solid #eee;">
                            <strong>Mobile ilova</strong> - React Native va Firebase asosida
                        </li>
                        <li style="padding: 0.5rem 0;">
                            <strong>Analitika platformasi</strong> - Python va D3.js asosida
                        </li>
                    </ul>
                    
                    <h3 style="margin-top: 2rem;">Maqsadlarim</h3>
                    <p>Kelajakda men AI va machine learning sohasini o'rganib, dasturlash va sun'iy intellektni birlashtiruvchi loyihalar yaratishni rejalashtiraman.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Stats Section -->
    <section class="stats-section">
        <div class="container">
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-icon">
                        <i class="fas fa-code"></i>
                    </div>
                    <div class="stat-number">50+</div>
                    <div class="stat-text">Bajarilgan Loyihalar</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">
                        <i class="fas fa-users"></i>
                    </div>
                    <div class="stat-number">35+</div>
                    <div class="stat-text">Xursand Mijozlar</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">
                        <i class="fas fa-clock"></i>
                    </div>
                    <div class="stat-number">5</div>
                    <div class="stat-text">Yillik Tajriba</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">
                        <i class="fas fa-award"></i>
                    </div>
                    <div class="stat-number">12</div>
                    <div class="stat-text">Sertifikatlar</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects-section">
        <div class="container">
            <div class="section-title">
                <h2>Mening Loyihalarim</h2>
                <p>So'nggi ishlarimdan ba'zilari</p>
            </div>
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-image">
                        <i class="fas fa-shopping-cart"></i>
                    </div>
                    <div class="project-content">
                        <h3>E-commerce Platform</h3>
                        <p>React va Node.js asosida yaratilgan to'liq funksional onlayn do'kon.</p>
                        <div class="project-tags">
                            <div class="project-tag">React</div>
                            <div class="project-tag">Node.js</div>
                            <div class="project-tag">MongoDB</div>
                        </div>
                        <a href="#" class="project-btn">Ko'rish</a>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-image">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <div class="project-content">
                        <h3>Analitika Dashboard</h3>
                        <p>Biznes ma'lumotlarini vizuallashtirish va tahlil qilish uchun dashboard.</p>
                        <div class="project-tags">
                            <div class="project-tag">Vue.js</div>
                            <div class="project-tag">D3.js</div>
                            <div class="project-tag">Python</div>
                        </div>
                        <a href="#" class="project-btn">Ko'rish</a>
                    </div>
                </div>
                <div class="project-card">
                    <div class="project-image">
                        <i class="fas fa-mobile-alt"></i>
                    </div>
                    <div class="project-content">
                        <h3>Task Manager App</h3>
                        <p>React Native da yaratilgan ko'p platformali vazifalar boshqaruv ilovasi.</p>
                        <div class="project-tags">
                            <div class="project-tag">React Native</div>
                            <div class="project-tag">Firebase</div>
                            <div class="project-tag">Redux</div>
                        </div>
                        <a href="#" class="project-btn">Ko'rish</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section id="contact" class="cta-section">
        <div class="container">
            <h2>Loyihangiz ustida hamkorlik qilaylikmi?</h2>
            <p>Men sizning g'oyalaringizni hayotga tatbiq etishga yordam berishdan xursandman. Keling, suhbatlashamiz!</p>
            <div class="cta-buttons">
                <a href="#" class="btn btn-primary">Portfolio Ko'rish</a>
                <a href="#" class="btn btn-outline">Bog'lanish</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-column">
                    <h3>Shohjahon Mardonov</h3>
                    <p>Full Stack Dasturchi & UI/UX Dizayner. Zamonaviy veb-ilovalar yaratishga ixtisoslashganman.</p>
                    <div class="footer-social">
                        <a href="#"><i class="fab fa-github"></i></a>
                        <a href="#"><i class="fab fa-linkedin-in"></i></a>
                        <a href="#"><i class="fab fa-telegram"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                    </div>
                </div>
                <div class="footer-column">
                    <h3>Tez Havolalar</h3>
                    <ul class="footer-links">
                        <li><a href="#">Bosh Sahifa</a></li>
                        <li><a href="#about">Haqimda</a></li>
                        <li><a href="#skills">Ko'nikmalar</a></li>
                        <li><a href="#projects">Loyihalar</a></li>
                        <li><a href="#contact">Aloqa</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3>Xizmatlar</h3>
                    <ul class="footer-links">
                        <li><a href="#">Veb Dasturlash</a></li>
                        <li><a href="#">Mobil Ilovalar</a></li>
                        <li><a href="#">UI/UX Dizayn</a></li>
                        <li><a href="#">SEO Optimizatsiya</a></li>
                        <li><a href="#">Konsultatsiya</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3>Aloqa</h3>
                    <ul class="footer-links">
                        <li><i class="fas fa-map-marker-alt"></i> Toshkent, O'zbekiston</li>
                        <li><i class="fas fa-phone"></i> +998 90 123 45 67</li>
                        <li><i class="fas fa-envelope"></i> shohjahon@example.uz</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2023 Shohjahon Mardonov. Barcha huquqlar himoyalangan.</p>
            </div>
        </div>
    </footer>

    <script>
        // Mobile menu toggle
        document.querySelector('.mobile-menu').addEventListener('click', function() {
            const navLinks = document.querySelector('.nav-links');
            
            if (navLinks.style.display === 'flex') {
                navLinks.style.display = 'none';
            } else {
                navLinks.style.display = 'flex';
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '100%';
                navLinks.style.left = '0';
                navLinks.style.width = '100%';
                navLinks.style.background = 'white';
                navLinks.style.padding = '1rem 0';
                navLinks.style.boxShadow = '0 5px 10px rgba(0,0,0,0.1)';
                
                const links = navLinks.querySelectorAll('li');
                links.forEach(link => {
                    link.style.margin = '0.5rem 0';
                    link.style.textAlign = 'center';
                });
            }
        });

        // Header background on scroll
        window.addEventListener('scroll', function() {
            const header = document.querySelector('header');
            if (window.scrollY > 50) {
                header.style.background = 'rgba(255, 255, 255, 0.95)';
                header.style.backdropFilter = 'blur(10px)';
            } else {
                header.style.background = 'rgba(255, 255, 255, 0.95)';
            }
        });

        // Animate stats counter
        function animateValue(element, start, end, duration) {
            let startTimestamp = null;
            const step = (timestamp) => {
                if (!startTimestamp) startTimestamp = timestamp;
                const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                element.innerHTML = Math.floor(progress * (end - start) + start) + "+";
                if (progress < 1) {
                    window.requestAnimationFrame(step);
                }
            };
            window.requestAnimationFrame(step);
        }

        // Start animation when stats section is in view
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const statNumbers = document.querySelectorAll('.stat-number');
                    statNumbers.forEach(stat => {
                        const target = parseInt(stat.textContent);
                        animateValue(stat, 0, target, 2000);
                    });
                    observer.disconnect();
                }
            });
        });

        observer.observe(document.querySelector('.stats-section'));
    </script>
</body>
</html>"""

contact = """<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Biz bilan bog'laning</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        :root {
            --primary: #6c63ff;
            --secondary: #ff6584;
            --accent: #42e695;
            --dark: #2a2a72;
            --light: #f8f9fa;
            --success: #4caf50;
            --warning: #ff9800;
            --info: #2196f3;
        }

        body {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .contact-container {
            display: flex;
            max-width: 1200px;
            width: 100%;
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
        }

        .contact-info {
            flex: 1;
            background: linear-gradient(135deg, var(--dark) 0%, var(--primary) 100%);
            color: white;
            padding: 40px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .contact-form {
            flex: 1.2;
            padding: 40px;
        }

        .contact-info h2 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            position: relative;
        }

        .contact-info h2::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 60px;
            height: 4px;
            background: var(--secondary);
            border-radius: 2px;
        }

        .contact-info p {
            margin-bottom: 30px;
            line-height: 1.6;
            opacity: 0.9;
        }

        .contact-details {
            margin-top: 20px;
        }

        .contact-item {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }

        .contact-icon {
            width: 50px;
            height: 50px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-right: 15px;
            font-size: 1.2rem;
        }

        .social-links {
            display: flex;
            margin-top: 30px;
        }

        .social-link {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            display: flex;
            justify-content: center;
            align-items: center;
            margin-right: 10px;
            color: white;
            text-decoration: none;
            transition: all 0.3s ease;
        }

        .social-link:hover {
            background: var(--secondary);
            transform: translateY(-3px);
        }

        .contact-form h2 {
            color: var(--dark);
            font-size: 2.2rem;
            margin-bottom: 30px;
            position: relative;
        }

        .contact-form h2::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 0;
            width: 60px;
            height: 4px;
            background: var(--accent);
            border-radius: 2px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: var(--dark);
        }

        .form-control {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e1e5ee;
            border-radius: 10px;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .form-control:focus {
            border-color: var(--primary);
            outline: none;
            box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.2);
        }

        textarea.form-control {
            min-height: 150px;
            resize: vertical;
        }

        .btn-group {
            display: flex;
            gap: 15px;
            margin-top: 10px;
        }

        .btn {
            padding: 12px 25px;
            border: none;
            border-radius: 10px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .btn-primary {
            background: var(--primary);
            color: white;
            flex: 2;
        }

        .btn-primary:hover {
            background: #5752d4;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(108, 99, 255, 0.4);
        }

        .btn-secondary {
            background: var(--secondary);
            color: white;
            flex: 1;
        }

        .btn-secondary:hover {
            background: #e05575;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 101, 132, 0.4);
        }

        .btn-accent {
            background: var(--accent);
            color: white;
            flex: 1;
        }

        .btn-accent:hover {
            background: #38c982;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(66, 230, 149, 0.4);
        }

        .btn i {
            margin-right: 8px;
        }

        @media (max-width: 768px) {
            .contact-container {
                flex-direction: column;
            }
            
            .btn-group {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="contact-container">
        <div class="contact-info">
            <h2>Biz bilan bog'laning</h2>
            <p>Savollaringiz bo'lsa yoki loyihangiz haqida suhbatlashmoqchi bo'lsangiz, quyidagi ma'lumotlar orqali biz bilan bog'lanishingiz mumkin.</p>
            
            <div class="contact-details">
                <div class="contact-item">
                    <div class="contact-icon">
                        <i class="fas fa-map-marker-alt"></i>
                    </div>
                    <div>
                        <h3>Manzil</h3>
                        <p>Samarqand shahar</p>
                    </div>
                </div>
                
                <div class="contact-item">
                    <div class="contact-icon">
                        <i class="fas fa-phone"></i>
                    </div>
                    <div>
                        <h3>Telefon</h3>
                        <p>+998 94 081 01 26</p>
                    </div>
                </div>
                
                <div class="contact-item">
                    <div class="contact-icon">
                        <i class="fas fa-envelope"></i>
                    </div>
                    <div>
                        <h3>Email</h3>
                        <p>info@example.uz</p>
                    </div>
                </div>
            </div>
            
            <div class="social-links">
                <a href="#" class="social-link">
                    <i class="fab fa-telegram"></i>
                </a>
                <a href="#" class="social-link">
                    <i class="fab fa-instagram"></i>
                </a>
                <a href="#" class="social-link">
                    <i class="fab fa-facebook-f"></i>
                </a>
                <a href="#" class="social-link">
                    <i class="fab fa-twitter"></i>
                </a>
            </div>
        </div>
        
        <div class="contact-form">
            <h2>Xabar yuboring</h2>
            <form id="contactForm">
                <div class="form-group">
                    <label for="name">Ism</label>
                    <input type="text" id="name" class="form-control" placeholder="Ismingizni kiriting" required>
                </div>
                
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" class="form-control" placeholder="Email manzilingiz" required>
                </div>
                
                <div class="form-group">
                    <label for="subject">Mavzu</label>
                    <input type="text" id="subject" class="form-control" placeholder="Xabar mavzusi" required>
                </div>
                
                <div class="form-group">
                    <label for="message">Xabar</label>
                    <textarea id="message" class="form-control" placeholder="Xabaringizni yozing..." required></textarea>
                </div>
                
                <div class="btn-group">
                    <button type="submit" class="btn btn-primary">
                        <i class="fas fa-paper-plane"></i> Xabarni yuborish
                    </button>
                    <button type="button" class="btn btn-secondary">
                        <i class="fas fa-phone"></i> Qo'ng'iroq
                    </button>
                    <button type="button" class="btn btn-accent">
                        <i class="fas fa-video"></i> Video chat
                    </button>
                </div>
            </form>
        </div>
    </div>

    <script>
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Form ma'lumotlarini olish
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const subject = document.getElementById('subject').value;
            const message = document.getElementById('message').value;
            
            // Bu yerda form ma'lumotlarini serverga yuborish logikasi bo'ladi
            console.log({
                name,
                email,
                subject,
                message
            });
            
            // Muvaffaqiyatli yuborilganini bildirish
            alert('Xabaringiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog\'lanamiz.');
            
            // Formni tozalash
            this.reset();
        });
        
        // Qo'ng'iroq qilish tugmasi
        document.querySelector('.btn-secondary').addEventListener('click', function() {
            alert('Qo\'ng\'iroq uchun: +998 90 123 45 67');
        });
        
        // Video chat tugmasi
        document.querySelector('.btn-accent').addEventListener('click', function() {
            alert('Video chat uchun siz bilan tez orada bog\'lanamiz');
        });
    </script>
</body>
</html>"""

profile = """<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mening Profilim</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        :root {
            --primary: #6c63ff;
            --primary-dark: #5752d4;
            --primary-light: #8a84ff;
            --secondary: #ff6584;
            --secondary-dark: #e05575;
            --accent: #42e695;
            --accent-dark: #38c982;
            --success: #4caf50;
            --warning: #ff9800;
            --info: #2196f3;
            --danger: #f44336;
            --dark: #2a2a72;
            --darker: #1e1e4e;
            --light: #f8f9fa;
            --gray: #6c757d;
            --light-gray: #e9ecef;
            --gradient-primary: linear-gradient(135deg, var(--primary) 0%, var(--dark) 100%);
            --gradient-secondary: linear-gradient(135deg, var(--secondary) 0%, var(--warning) 100%);
            --gradient-accent: linear-gradient(135deg, var(--accent) 0%, var(--info) 100%);
            --gradient-dark: linear-gradient(135deg, var(--dark) 0%, #0f0f2d 100%);
            --shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 15px 30px rgba(0, 0, 0, 0.15);
        }

        body {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            padding: 20px;
            color: var(--dark);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .profile-header {
            background: var(--gradient-primary);
            border-radius: 20px;
            padding: 30px;
            color: white;
            display: flex;
            align-items: center;
            margin-bottom: 30px;
            box-shadow: var(--shadow-lg);
            position: relative;
            overflow: hidden;
        }

        .profile-header::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 100%;
            height: 200%;
            background: rgba(255, 255, 255, 0.1);
            transform: rotate(30deg);
        }

        .profile-avatar {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 5px solid rgba(255, 255, 255, 0.3);
            overflow: hidden;
            margin-right: 30px;
            position: relative;
            z-index: 2;
            background: var(--light);
        }

        .profile-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .profile-info {
            flex: 1;
            position: relative;
            z-index: 2;
        }

        .profile-name {
            font-size: 2.2rem;
            margin-bottom: 5px;
            font-weight: 700;
        }

        .profile-title {
            font-size: 1.2rem;
            opacity: 0.9;
            margin-bottom: 15px;
        }

        .profile-stats {
            display: flex;
            gap: 20px;
        }

        .stat {
            text-align: center;
        }

        .stat-value {
            font-size: 1.5rem;
            font-weight: 700;
        }

        .stat-label {
            font-size: 0.9rem;
            opacity: 0.8;
        }

        .profile-content {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 30px;
        }

        .sidebar {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .main-content {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: var(--shadow);
        }

        .card-header {
            display: flex;
            justify-content: between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px solid var(--light-gray);
        }

        .card-title {
            font-size: 1.4rem;
            font-weight: 600;
            color: var(--dark);
        }

        .btn {
            padding: 10px 20px;
            border: none;
            border-radius: 10px;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .btn-sm {
            padding: 8px 15px;
            font-size: 0.85rem;
        }

        .btn-lg {
            padding: 12px 25px;
            font-size: 1rem;
        }

        .btn-primary {
            background: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background: var(--primary-dark);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(108, 99, 255, 0.4);
        }

        .btn-secondary {
            background: var(--secondary);
            color: white;
        }

        .btn-secondary:hover {
            background: var(--secondary-dark);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 101, 132, 0.4);
        }

        .btn-accent {
            background: var(--accent);
            color: white;
        }

        .btn-accent:hover {
            background: var(--accent-dark);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(66, 230, 149, 0.4);
        }

        .btn-success {
            background: var(--success);
            color: white;
        }

        .btn-success:hover {
            background: #3d8b40;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
        }

        .btn-warning {
            background: var(--warning);
            color: white;
        }

        .btn-warning:hover {
            background: #e68900;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 152, 0, 0.4);
        }

        .btn-info {
            background: var(--info);
            color: white;
        }

        .btn-info:hover {
            background: #0b7dda;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(33, 150, 243, 0.4);
        }

        .btn-danger {
            background: var(--danger);
            color: white;
        }

        .btn-danger:hover {
            background: #d32f2f;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(244, 67, 54, 0.4);
        }

        .btn-dark {
            background: var(--dark);
            color: white;
        }

        .btn-dark:hover {
            background: var(--darker);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(42, 42, 114, 0.4);
        }

        .btn-outline {
            background: transparent;
            border: 2px solid var(--primary);
            color: var(--primary);
        }

        .btn-outline:hover {
            background: var(--primary);
            color: white;
        }

        .btn-group {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .about-text {
            line-height: 1.6;
            color: var(--gray);
        }

        .skills-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }

        .skill-tag {
            background: var(--light);
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 0.9rem;
            color: var(--dark);
            border-left: 4px solid var(--primary);
        }

        .activity-item {
            display: flex;
            align-items: center;
            padding: 15px 0;
            border-bottom: 1px solid var(--light-gray);
        }

        .activity-item:last-child {
            border-bottom: none;
        }

        .activity-icon {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--light);
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 15px;
            color: var(--primary);
        }

        .activity-content {
            flex: 1;
        }

        .activity-title {
            font-weight: 600;
            margin-bottom: 5px;
        }

        .activity-desc {
            font-size: 0.9rem;
            color: var(--gray);
        }

        .activity-time {
            font-size: 0.8rem;
            color: var(--gray);
        }

        .badge {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-left: 10px;
        }

        .badge-primary {
            background: var(--primary);
            color: white;
        }

        .badge-secondary {
            background: var(--secondary);
            color: white;
        }

        .badge-success {
            background: var(--success);
            color: white;
        }

        .badge-warning {
            background: var(--warning);
            color: white;
        }

        .progress-bar {
            height: 10px;
            background: var(--light-gray);
            border-radius: 5px;
            overflow: hidden;
            margin-top: 10px;
        }

        .progress-fill {
            height: 100%;
            border-radius: 5px;
        }

        .progress-primary {
            background: var(--primary);
        }

        .progress-success {
            background: var(--success);
        }

        .progress-warning {
            background: var(--warning);
        }

        .social-links {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }

        .social-link {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: var(--light);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--dark);
            text-decoration: none;
            transition: all 0.3s ease;
        }

        .social-link:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
        }

        .social-telegram {
            background: #0088cc;
            color: white;
        }

        .social-instagram {
            background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
            color: white;
        }

        .social-facebook {
            background: #3b5998;
            color: white;
        }

        .social-twitter {
            background: #1da1f2;
            color: white;
        }

        .social-linkedin {
            background: #0077b5;
            color: white;
        }

        @media (max-width: 992px) {
            .profile-content {
                grid-template-columns: 1fr;
            }
            
            .profile-header {
                flex-direction: column;
                text-align: center;
            }
            
            .profile-avatar {
                margin-right: 0;
                margin-bottom: 20px;
            }
            
            .profile-stats {
                justify-content: center;
            }
        }

        @media (max-width: 576px) {
            .profile-stats {
                flex-wrap: wrap;
            }
            
            .btn-group {
                flex-direction: column;
            }
            
            .btn {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Profil sarlavhasi -->
        <div class="profile-header">
            <div class="profile-avatar">
                <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="Profil rasmi">
            </div>
            <div class="profile-info">
                <h1 class="profile-name">Azizbek Ismoilov <span class="badge badge-success">Premium</span></h1>
                <p class="profile-title">Senior Dasturchi & UI/UX Dizayner</p>
                <p>Dasturlashga qiziquvchi va yangi texnologiyalarni o'rganishni sevuvchi mutaxassis</p>
                
                <div class="profile-stats">
                    <div class="stat">
                        <div class="stat-value">247</div>
                        <div class="stat-label">Loyihalar</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">5.0</div>
                        <div class="stat-label">Reyting</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">128</div>
                        <div class="stat-label">Mijozlar</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">5 yil</div>
                        <div class="stat-label">Tajriba</div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Asosiy kontent -->
        <div class="profile-content">
            <!-- Yon panel -->
            <div class="sidebar">
                <!-- Profil sozlamalari -->
                <div class="card">
                    <div class="card-header">
                        <h2 class="card-title">Profil Sozlamalari</h2>
                    </div>
                    <div class="btn-group">
                        <button class="btn btn-primary btn-sm"><i class="fas fa-edit"></i> Tahrirlash</button>
                        <button class="btn btn-outline btn-sm"><i class="fas fa-share-alt"></i> Ulashish</button>
                        <button class="btn btn-success btn-sm"><i class="fas fa-download"></i> Yuklab olish</button>
                    </div>
                </div>
                
                <!-- Kontakt ma'lumotlari -->
                <div class="card">
                    <div class="card-header">
                        <h2 class="card-title">Kontakt Ma'lumotlari</h2>
                    </div>
                    <p><i class="fas fa-envelope"></i> azizbek@example.uz</p>
                    <p><i class="fas fa-phone"></i> +998 90 123 45 67</p>
                    <p><i class="fas fa-map-marker-alt"></i> Toshkent, O'zbekiston</p>
                    
                    <div class="social-links">
                        <a href="#" class="social-link social-telegram"><i class="fab fa-telegram"></i></a>
                        <a href="#" class="social-link social-instagram"><i class="fab fa-instagram"></i></a>
                        <a href="#" class="social-link social-facebook"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="social-link social-twitter"><i class="fab fa-twitter"></i></a>
                        <a href="#" class="social-link social-linkedin"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
                
                <!-- Ko'nikmalar -->
                <div class="card">
                    <div class="card-header">
                        <h2 class="card-title">Texnologiyalar</h2>
                    </div>
                    <div class="skills-list">
                        <span class="skill-tag">HTML/CSS</span>
                        <span class="skill-tag">JavaScript</span>
                        <span class="skill-tag">React</span>
                        <span class="skill-tag">Vue.js</span>
                        <span class="skill-tag">Node.js</span>
                        <span class="skill-tag">Python</span>
                        <span class="skill-tag">Django</span>
                        <span class="skill-tag">UI/UX Dizayn</span>
                    </div>
                </div>
                
                <!-- Statistika -->
                <div class="card">
                    <div class="card-header">
                        <h2 class="card-title">Statistika</h2>
                    </div>
                    <p>Profil to'liqligi</p>
                    <div class="progress-bar">
                        <div class="progress-fill progress-primary" style="width: 85%"></div>
                    </div>
                    
                    <p>Loyihalar muvaffaqiyati</p>
                    <div class="progress-bar">
                        <div class="progress-fill progress-success" style="width: 92%"></div>
                    </div>
                    
                    <p>Mijozlar qoniqishi</p>
                    <div class="progress-bar">
                        <div class="progress-fill progress-warning" style="width: 96%"></div>
                    </div>
                </div>
            </div>
            
            <!-- Asosiy kontent -->
            <div class="main-content">
                <!-- Profil haqida -->
                <div class="card">
                    <div class="card-header">
                        <h2 class="card-title">Men haqimda</h2>
                        <button class="btn btn-outline btn-sm"><i class="fas fa-edit"></i> Tahrirlash</button>
                    </div>
                    <p class="about-text">
                        5 yildan ortiq tajribaga ega senior dasturchi va UI/UX dizayner. 
                        Turli xil veb-ilovalar, mobil ilovalar va veb-saytlarni ishlab chiqishda keng tajribam mavjud. 
                        Yangi texnologiyalarni o'rganish va jamoaviy loyihalarda ishlashni yaxshi ko'raman.
                    </p>
                    <p class="about-text">
                        Hozirda bir nechta startap loyihalarda ishtirok etmoqdaman va 
                        dasturlash bo'yicha yangi boshlanuvchilarga mentorlik qilaman.
                    </p>
                </div>
                
                <!-- So'nggi faoliyat -->
                <div class="card">
                    <div class="card-header">
                        <h2 class="card-title">So'nggi Faoliyat</h2>
                        <button class="btn btn-outline btn-sm"><i class="fas fa-filter"></i> Filtr</button>
                    </div>
                    
                    <div class="activity-item">
                        <div class="activity-icon">
                            <i class="fas fa-code"></i>
                        </div>
                        <div class="activity-content">
                            <div class="activity-title">Yangi loyiha boshlandi</div>
                            <div class="activity-desc">"Smart Edu" platformasi uchun frontend qismi ishlab chiqilmoqda</div>
                        </div>
                        <div class="activity-time">2 soat oldin</div>
                    </div>
                    
                    <div class="activity-item">
                        <div class="activity-icon">
                            <i class="fas fa-tasks"></i>
                        </div>
                        <div class="activity-content">
                            <div class="activity-title">Loyiha yakunlandi</div>
                            <div class="activity-desc">"E-commerce" platformasi muvaffaqiyatli yakunlandi va mijozga topshirildi</div>
                        </div>
                        <div class="activity-time">1 kun oldin</div>
                    </div>
                    
                    <div class="activity-item">
                        <div class="activity-icon">
                            <i class="fas fa-medal"></i>
                        </div>
                        <div class="activity-content">
                            <div class="activity-title">Mukofot olindi</div>
                            <div class="activity-desc">"Yilning eng yaxshi dasturchisi" mukofoti bilan taqdirlandi</div>
                        </div>
                        <div class="activity-time">3 kun oldin</div>
                    </div>
                    
                    <div class="activity-item">
                        <div class="activity-icon">
                            <i class="fas fa-users"></i>
                        </div>
                        <div class="activity-content">
                            <div class="activity-title">Yangi mijoz</div>
                            <div class="activity-desc">Xalqaro kompaniya bilan yangi loyiha bo'yicha shartnoma imzolandi</div>
                        </div>
                        <div class="activity-time">1 hafta oldin</div>
                    </div>
                </div>
                
                <!-- Tugmalar guruhi -->
                <div class="card">
                    <div class="card-header">
                        <h2 class="card-title">Tezkor Amallar</h2>
                    </div>
                    <div class="btn-group">
                        <button class="btn btn-primary"><i class="fas fa-plus"></i> Yangi Loyiha</button>
                        <button class="btn btn-secondary"><i class="fas fa-upload"></i> Portfolio Qo'shish</button>
                        <button class="btn btn-accent"><i class="fas fa-bell"></i> Bildirishnomalar</button>
                        <button class="btn btn-success"><i class="fas fa-chart-line"></i> Statistika</button>
                        <button class="btn btn-warning"><i class="fas fa-cog"></i> Sozlamalar</button>
                        <button class="btn btn-info"><i class="fas fa-question-circle"></i> Yordam</button>
                        <button class="btn btn-danger"><i class="fas fa-sign-out-alt"></i> Chiqish</button>
                        <button class="btn btn-dark"><i class="fas fa-moon"></i> Tema</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Tugmalarga interaktivlik qo'shish
        document.querySelectorAll('.btn').forEach(button => {
            button.addEventListener('click', function() {
                // Bu yerda har bir tugma bosilganda bajariladigan kod bo'ladi
                const buttonText = this.textContent.trim();
                alert(`"${buttonText}" tugmasi bosildi!`);
            });
        });
        
        // Tema o'zgartirish
        document.querySelector('.btn-dark').addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
            if (document.body.classList.contains('dark-mode')) {
                this.innerHTML = '<i class="fas fa-sun"></i> Tema';
            } else {
                this.innerHTML = '<i class="fas fa-moon"></i> Tema';
            }
        });
    </script>
</body>
</html>"""