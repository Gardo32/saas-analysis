from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, current_app, session, \
    flash
from flask_login import login_required, current_user
import pandas as pd
import os
import matplotlib.pyplot as plt
import io
import base64

csv_handler_bp = Blueprint('csv_handler', __name__)


@csv_handler_bp.route('/upload_csv')
@login_required
def upload_csv():
    return render_template('upload.html')


@csv_handler_bp.route('/upload_csv', methods=['POST'])
@login_required
def upload_csv_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        session['uploaded_file'] = file.filename
        return redirect(url_for('csv_handler.process_csv_file', filename=file.filename))
    flash('Invalid file format')
    return redirect(request.url)


@csv_handler_bp.route('/process_csv/<filename>')
@login_required
def process_csv_file(filename):
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    df = pd.read_csv(filepath)
    columns = df.columns.tolist()
    return render_template('process.html', columns=columns, filename=filename)


@csv_handler_bp.route('/plot_csv', methods=['POST'])
@login_required
def plot_csv():
    filename = session.get('uploaded_file')
    if not filename:
        flash('No file uploaded')
        return redirect(url_for('csv_handler.upload_csv'))

    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    df = pd.read_csv(filepath)

    chart_title = request.form['chart_title']
    myindex = request.form['index_column']
    cols = request.form['plot_column']

    if myindex not in df.columns or cols not in df.columns:
        flash('Invalid columns selected')
        return redirect(url_for('csv_handler.process_csv_file', filename=filename))

    df = df.drop_duplicates(subset=myindex).head(10)
    df.set_index(myindex)[cols].plot(kind="bar")

    plt.title(chart_title)
    plt.xlabel(myindex.upper())
    plt.ylabel(cols.upper())

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()

    return render_template('plot.html', plot_url=plot_url)


@csv_handler_bp.route('/delete_csv/<filename>', methods=['POST'])
@login_required
def delete_csv(filename):
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    if os.path.isfile(filepath):
        os.remove(filepath)
        session.pop('uploaded_file', None)
        flash('File deleted successfully')
    else:
        flash('File not found')
    return redirect(url_for('csv_handler.upload_csv'))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'csv'}
