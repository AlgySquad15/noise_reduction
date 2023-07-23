from PIL import Image, ImageFilter

# Mendapatkan input nama file gambar
filename = input("Masukkan nama file gambar (dengan ekstensi): ")

# Mendapatkan input lokasi dan nama file output
output_filename = input("Masukkan nama file output (dengan ekstensi): ")

# Mendapatkan input level reduksi noise
noise_reduction = int(input("Masukkan level reduksi noise (0-9): "))

# Membuka gambar menggunakan Pillow
image = Image.open(filename)

# Mengurangi noise pada gambar
denoised_image = image.filter(ImageFilter.GaussianBlur(noise_reduction))

# Menghitung resolusi gambar asli
width, height = denoised_image.size

# Menghitung resolusi 4K (3840x2160)
fourk_width, fourk_height = 3840, 2160

# Menghitung faktor skala untuk 4K
fourk_scale_factor = min(fourk_width / width, fourk_height / height)

# Menghitung ukuran gambar setelah di-resize ke 4K
resized_fourk_width = int(width * fourk_scale_factor)
resized_fourk_height = int(height * fourk_scale_factor)

# Melakukan resize gambar ke resolusi 4K dengan metode Lanczos
resized_fourk_image = denoised_image.resize((resized_fourk_width, resized_fourk_height), Image.LANCZOS)

# Membuat canvas kosong dengan ukuran 4K
fourk_canvas = Image.new("RGB", (fourk_width, fourk_height))

# Menghitung posisi gambar yang di-resize di tengah canvas 4K
fourk_offset_x = (fourk_width - resized_fourk_width) // 2
fourk_offset_y = (fourk_height - resized_fourk_height) // 2

# Menempatkan gambar di tengah canvas 4K
fourk_canvas.paste(resized_fourk_image, (fourk_offset_x, fourk_offset_y))

# Simpan gambar hasil resize ke file output dengan resolusi 4K
fourk_canvas.save(output_filename, "JPEG", quality=100, subsampling=0)

print("Gambar berhasil di-resize ke resolusi 4K dengan reduksi noise.")
