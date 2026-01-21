# 📌 AUTOMATION TEST SCENARIO — ORANGE HRM

---

## 📌 FEATURE: LOGIN

> Login digunakan sebagai **fixture** (`@pytest.fixture`) dan menjadi precondition untuk seluruh test PIM.

### ✅ SCENARIO 1 — Login dengan data valid

* **Precondition:** User berada di halaman login
* **Given** user membuka halaman login
* **When** user mengisi username dan password valid
* **Then** user berhasil login dan masuk ke dashboard
* **Digunakan di:** Semua test PIM (`login` fixture)
* **Test Data:**

  * Username: `cymera`
  * Password: `admin123`

> ❌ Negative scenario login (password salah / field kosong) **belum di-cover** di automation test.

---

## 📌 FEATURE: PIM (Personnel Info Management)

### 🟢 SMOKE TEST

#### ✅ SCENARIO 1 — Tambah Employee

* **Precondition:** User login dan berada di menu PIM
* **Given** user membuka form Add Employee
* **When** user mengisi First Name, Last Name, dan Employee ID lalu klik Save
* **Then** employee berhasil ditambahkan dan muncul notifikasi sukses
* **Automation Test:** `test_add_employee`

---

#### ✅ SCENARIO 2 — Tambah dan Cari Employee

* **Precondition:** User login dan berada di menu PIM
* **Given** user menambahkan employee baru
* **When** user kembali ke list dan melakukan pencarian berdasarkan First Name
* **Then** data employee tampil di tabel hasil pencarian
* **Automation Test:** `test_add_and_search_employee`

---

#### ✅ SCENARIO 3 — Tambah, Cari, dan Edit Employee

* **Precondition:** User login dan berada di menu PIM
* **Given** user menambahkan employee baru
* **When** user mencari employee tersebut dan mengubah Last Name
* **Then** data employee berhasil diupdate dan muncul notifikasi sukses
* **Automation Test:** `test_add_search_edit_employee`

---

### 🟡 REGRESSION TEST

#### ✅ SCENARIO 4 — Search Employee (Data Ditemukan)

* **Precondition:** Employee sudah ada di sistem
* **Given** user berada di halaman PIM List
* **When** user mencari employee berdasarkan nama
* **Then** data employee muncul di tabel
* **Automation Test:** `test_search_employee`

---

#### ✅ SCENARIO 5 — Search Employee (Data Tidak Ditemukan)

* **Precondition:** User berada di halaman PIM List
* **Given** user melakukan pencarian employee
* **When** data tidak ada di sistem
* **Then** muncul pesan "No Records Found"
* **Automation Test:** `test_search_employee_not_found`

---

#### ✅ SCENARIO 6 — Edit Employee

* **Precondition:** Employee sudah ada di sistem
* **Given** user membuka detail employee
* **When** user mengubah data employee (Last Name)
* **Then** perubahan berhasil disimpan dan muncul notifikasi sukses
* **Automation Test:** `test_edit_employee`

---

#### ✅ SCENARIO 7 — Hapus Employee

* **Precondition:** Employee sudah ada di sistem
* **Given** user mencari employee berdasarkan ID
* **When** user menghapus employee
* **Then** employee berhasil dihapus dan muncul notifikasi sukses
* **Automation Test:** `test_search_and_delete_employee`

---

### 🔴 VALIDATION TEST

#### ✅ SCENARIO 8 — Validasi Field Wajib Add Employee

* **Precondition:** User login dan membuka form Add Employee
* **Given** user berada di form Add Employee
* **When** user klik Save tanpa mengisi field wajib
* **Then** muncul pesan error "Required"
* **Automation Test:** `test_add_employee_required_field`

---

## 📌 CATATAN

* Smoke Test difokuskan ke **alur utama bisnis (happy path)**
* Regression Test mencakup **search, edit, delete, dan edge case**
* Semua scenario sudah **sinkron dengan implementasi `test_pim.py`**

---

## ▶️ MENJALANKAN TEST

```bash
pytest tests/test_pim.py -s
```

Test tertentu:

```bash
pytest tests/test_pim.py::test_edit_employee -s
```

---

## 🚀 Cara Instalasi & Menjalankan Project (Dari Awal)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/CahyoAprianto112/orangehrm-selenium-pytest.git
cd orangeHRM
```

### 2️⃣ Buat & Aktifkan Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependency

```bash
pip install -r requirements.txt
```

### 4️⃣ Pastikan Browser & WebDriver

* Browser: Microsoft Edge / Chrome (sesuai config)
* Versi browser harus sesuai dengan driver
* Selenium Manager handle driver otomatis

### 5️⃣ Jalankan Test

**Semua test:**

```bash
pytest -v
```

**Smoke test saja:**

```bash
pytest -m smoke -v
```

**Regression test saja:**

```bash
pytest -m regression -v
```

**Test tertentu:**

```bash
pytest tests/test_pim.py::test_add_employee -s
```

### 6️⃣ Generate Report (Opsional)

```bash
pytest --html=report.html
```

---

### ℹ️ Catatan

* Pastikan OrangeHRM bisa diakses (local / demo)
* Credential login ada di fixture `login`
* Selesai pakai venv jangan lupa `deactivate`
