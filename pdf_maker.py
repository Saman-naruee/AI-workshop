from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def create_resume_pdf(output_path, lines, margin=40, line_spacing=15):
    """
    Creates a PDF resume with right-to-left text alignment.
    
    Args:
        output_path (str): Path where the PDF will be saved
        lines (list): List of text lines to write
        margin (int): Right margin in points
        line_spacing (int): Vertical space between lines in points
    
    Returns:
        str: Path to the created PDF file
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Create canvas and get dimensions
        c = canvas.Canvas(output_path, pagesize=A4)
        width, height = A4
        
        # Draw text lines
        y = height - margin
        for line in lines:
            c.drawRightString(width - margin, y, line)
            y -= line_spacing
        
        c.save()
        return output_path
    
    except Exception as e:
        print(f"Error creating PDF: {str(e)}")
        return None

# Resume content
RESUME_LINES = [
    "رزومه سامان ناروئی",
    "",
    "📧 samannaruee@gmail.com | ☎️ ۰۹۹۰۶۰۵۲۷۹۰",
    "📍 زاهدان، ایران | 🌐 github.com/Saman-naruee | 📎 linkedin.com/in/saman-naruee-nosrati",
    "",
    "برنامه‌نویس Python (توسعه‌دهنده API) | آماده برای همکاری دورکاری",
    "",
    "🧭 پروفایل حرفه‌ای",
    "برنامه‌نویس بک‌اند با تمرکز بر توسعه سرویس‌های مقیاس‌پذیر و RESTful API با استفاده از Django.",
    "تجربه در طراحی سیستم‌های واقعی برای کسب‌و‌کارها از جمله همکاری با تیم دیجی‌کالا.",
    "مسلط بر Git، Docker، Redis و PostgreSQL.",
    "علاقه‌مند به یادگیری و استفاده از ابزارهای هوش مصنوعی مانند OpenRouter, Groq, Cohere, Copilot و Google Gemini.",
    "",
    "🧰 مهارت‌ها",
    "- زبان‌ها و فریم‌ورک‌ها: Python, Django, DRF",
    "- ابزارها: Git, Docker, Celery, Redis, Postman",
    "- دیتابیس‌ها: PostgreSQL, SQLite",
    "- هوش مصنوعی و ابزارهای کدنویسی مدرن: OpenRouter, Groq, Github Copilot, Cohere, Google Gemini",
    "- اصول توسعه: RESTful API Design, Clean Code, JWT Auth",
    "- دیگر: کار تیمی، Agile, تجربه دورکاری",
    "",
    "💼 تجربه‌های حرفه‌ای",
    "🔹 پروژه لندینگ دیجی‌کالا (کارآموزی کاریار استودیو - ۱۴۰۳)",
    "• طراحی APIهای نسخه‌پذیر با DRF",
    "• پیاده‌سازی تاریخچه تغییرات با Django Simple History",
    "• اعتبارسنجی هوشمند داده‌ها و مجوزهای سفارشی",
    "🔗 github.com/karyar-studio/digimehr-landing-backend",
    "",
    "🔹 پروژه فروشگاه اینترنتی (خودآموز - ۱۴۰۲)",
    "• طراحی کامل API محصولات، سفارشات، کاربران",
    "• مستندسازی با Swagger، احراز هویت JWT",
    "• بهینه‌سازی کوئری‌ها با ORM",
    "🔗 github.com/Saman-naruee/OnlineShopKaryar",
    "",
    "🎓 دوره‌های تخصصی",
    "• گواهی Python مقدماتی – کوئرا",
    "• گواهی Python پیشرفته – کوئرا",
    "🔗 quera.org/user/SamanNaruee",
    "",
    "🌟 ویژگی‌های فردی",
    "- مشتاق یادگیری مداوم",
    "- روحیه تیمی بالا",
    "- علاقه‌مند به هوش مصنوعی و فناوری‌های نوین"
]

def main():
    """Main execution function"""
    pdf_path = os.path.join(os.path.expanduser("~"), "Desktop", "Saman-Naruee-Customized-Resume.pdf")
    result = create_resume_pdf(pdf_path, RESUME_LINES)
    
    if result:
        print(f"PDF successfully created at: {result}")
    else:
        print("Failed to create PDF")

if __name__ == "__main__":
    main()
