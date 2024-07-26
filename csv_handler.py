from flask import Blueprint, render_template, request, redirect, url_for, send_file, current_app
from flask_login import login_required, current_user
import pandas as pd
import matplotlib.pyplot as plt
import io
import os

csv_handler_bp = Blueprint('csv_handler', __name__)

# Ensure the upload folder exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')


@csv_handler_bp.route('/upload_csv', methods=['GET', 'POST'])
@login_required
def upload_csv():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return redirect(url_for('csv_handler.process_csv_file', filename=file.filename))

    return render_template('upload.html')


@csv_handler_bp.route('/process_csv/<filename>', methods=['GET', 'POST'])
@login_required
def process_csv_file(filename):
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

    if request.method == 'POST':
        index_col = request.form['index'].strip()
        data_col = request.form['columns'].strip()
        img = handle_file_upload(filepath, index_col, data_col)

        # Clean up the uploaded file after processing
        cleanup_file(filepath)

        return send_file(img, mimetype='image/png', as_attachment=True, download_name='comparison_plot.png')

    # Default processing (e.g., displaying the CSV)
    df = pd.read_csv(filepath)
    df = df.head(5)

    return render_template('display.html', tables=[df.to_html(classes='data', header="true", index=False)],
                           titles=df.columns.values, filename=filename)


@csv_handler_bp.route('/download_csv/<filename>')
@login_required
def download_csv_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv'}


def handle_file_upload(file_path, index_col, data_col):
    df = pd.read_csv(file_path)
    df = df.drop_duplicates(subset=index_col).head(10)

    plt.figure()
    df.set_index(index_col)[data_col].plot(kind="bar")
    plt.title("Comparison of Selected Columns")
    plt.xlabel(index_col.upper())
    plt.ylabel(data_col.upper())

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return img


def cleanup_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
