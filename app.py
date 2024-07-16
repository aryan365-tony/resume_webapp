from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
from flask import send_file
from io import BytesIO
import pdfkit
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db=SQLAlchemy(app)


@app.route("/")
def home_page():
    about_me_data=AboutMe.query.first()
    return render_template('FrontPage.html',about_me_data=about_me_data)

@app.route('/edu-page')
def edu_page():
    education_data = Education.query.all()
    return render_template('EduPage.html',educations=education_data)

@app.route('/por-page')
def por_page():
    pors=POR.query.all()
    return render_template('POR.html',pors=pors)

@app.route('/result-page')
def result_page():
    result=Result.query.all()
    return render_template('results.html',result=result)

@app.route('/projects-page')
def projects_page():
    projects=Project.query.all()
    return render_template('projects.html',projects=projects)

@app.route('/work-page')
def work_page():
    work=Work.query.all()
    return render_template('work.html',works=work)

@app.route('/skills-page')
def skill_page():
    skills=Skill.query.all()
    return render_template('skills.html',skills=skills)

@app.route('/download-page')
def download_page():
    return render_template('download.html')

@app.route('/editer',methods=['GET','POST'])
def edit_page():
    if request.method == 'POST':
        form_type = request.form.get('form_type')

        if form_type is None:
            # If no form_type is provided, default to 'about_me'
            pass

        if form_type == 'about_me':
            # process About Me form data
            update = request.form.get('update')
            about_me_paragraph = request.form['paragraph']
            about_me_image_url = request.form['imgURL']
            # create a new AboutMe object and add it to the database
            if update:
                sno = request.form.get('serial_no')
                data = AboutMe.query.get(sno)
                if about_me_paragraph:
                    data.paragraph = about_me_paragraph
                if about_me_image_url:
                    data.photo = about_me_image_url
            else:
                about_me = AboutMe(paragraph=about_me_paragraph, photo=about_me_image_url)
                db.session.add(about_me)
            db.session.commit()

        elif form_type == 'work':
            # process Work form data
            update = request.form.get('update')
            name = request.form['name']
            category = request.form['category']
            position = request.form['position']
            company = request.form['company']
            duration = request.form['duration']
            description = request.form['description']
            image_url = request.form['imgURL']
            # create a new Work object and add it to the database
            if update:
                sno = request.form.get('serial_no')
                data = Work.query.get(sno)
                if name:
                    data.name = name
                if category:
                    data.category = category
                if position:
                    data.position = position
                if company:
                    data.company = company
                if duration:
                    data.duration = duration
                if description:
                    data.description = description
                if image_url:
                    data.image_url = image_url
            else:
                work = Work(name=name, category=category, position=position, company=company, duration=duration, description=description, image_url=image_url)
                db.session.add(work)
            db.session.commit()

        elif form_type == 'project':
            # process Projects form data
            update = request.form.get('update')
            project_name = request.form['name']
            project_description = request.form['description']
            project_category = request.form['category']
            project_github = request.form['github']
            project_image_url = request.form['imgURL']
            # create a new Project object and add it to the database
            if update:
                sno = request.form.get('serial_no')
                data = Project.query.get(sno)
                if project_name:
                    data.name = project_name
                if project_description:
                    data.description = project_description
                if project_category:
                    data.category = project_category
                if project_github:
                    data.github_repo = project_github
                if project_image_url:
                    data.image_url = project_image_url
            else:
                project = Project(name=project_name, category=project_category, github_repo=project_github, description=project_description, image_url=project_image_url)
                db.session.add(project)
            db.session.commit()

        elif form_type == 'education':
            # process Education form data
            update = request.form.get('update')
            degree = request.form['degree']
            institution = request.form['institution']
            description = request.form['description']
            imgURL = request.form['imgURL']
            # create a new Education object and add it to the database
            if update:
                sno = request.form.get('serial_no')
                data = Education.query.get(sno)
                if degree:
                    data.degree = degree
                if institution:
                    data.institution = institution
                if description:
                    data.description = description
                if imgURL:
                    data.image_url= imgURL
            else:
                education = Education(degree=degree, institution=institution, description=description, image_url=imgURL)
                db.session.add(education)
            db.session.commit()

        elif form_type == 'por':
            # process PORs form data
            update = request.form.get('update')
            name = request.form['name']
            position = request.form['position']
            description = request.form['description']
            due_date = request.form['due_date']
            imgURL = request.form['imgURL']
            # create a new POR object and add it to the database
            if update:
                sno = request.form.get('serial_no')
                data = POR.query.get(sno)
                if name:
                   data.name = name
                if position:
                    data.position = position
                if description:
                    data.description = description
                if due_date:
                    data.due_date = due_date
                if imgURL:
                    data.image_url = imgURL
            else:
                por = POR(name=name, position=position, description=description, due_date=due_date, image_url=imgURL)
                db.session.add(por)
            db.session.commit()

        elif form_type == 'result':
            # process Results form data
            update = request.form.get('update')
            name = request.form['name']
            score = request.form['score']
            institution = request.form['institution']
            imgURL = request.form['imgURL']
            # create a new Result object and add it to the database
            if update:
                sno = request.form.get('serial_no')
                data = Result.query.get(sno)
                if name:
                    data.name = name
                if score:
                    data.score = score
                if institution:
                    data.institution = institution
                if imgURL:
                    data.image_url = imgURL
            else:
                result = Result(name=name, score=score, institution=institution, image_url=imgURL)
                db.session.add(result)
            db.session.commit()

        elif form_type == 'skill':
            # process Skills form data
            update = request.form.get('update')
            skill_name = request.form['name']
            description = request.form['description']
            link = request.form['link']
            date = request.form['date']
            imgURL = request.form['imgURL']
            company = request.form['company']
            # create a new Skill object and add it to the database
            if update:
                sno = request.form.get('serial_no')
                data = Skill.query.get(sno)
                if skill_name:
                    data.name = skill_name
                if description:
                    data.description = description
                if link:
                    data.link = link
                if date:
                    data.date = date
                if imgURL:
                    data.image_url = imgURL
                if company:
                    data.company = company
            else:
                skill = Skill(name=skill_name, description=description, link=link, date=date, image_url=imgURL, company=company)
                db.session.add(skill)
            db.session.commit()

        # Redirect to the same page to show the updated data
        return redirect(url_for('edit_page'))


    about_me_data=AboutMe.query.first()
    education_data = Education.query.all()
    pors=POR.query.all()
    result=Result.query.all()
    projects=Project.query.all()
    work=Work.query.all()
    skills=Skill.query.all()
    return render_template('editer.html', about_me_data=about_me_data, education_data=education_data, pors=pors, result=result, projects=projects, work=work, skills=skills)



#config = pdfkit.configuration(wkhtmltopdf='/static/wkhtmltopdf/bin/wkhtmltopdf.exe')

@app.route('/down-resume', methods=['GET'])
def resume():
    about_me_data=AboutMe.query.first()
    education_data = Education.query.all()
    pors=POR.query.all()
    result=Result.query.all()
    projects=Project.query.all()
    work=Work.query.all()
    skills=Skill.query.all()
    htmlFile=render_template('resume.html', about_me_data=about_me_data, education_data=education_data, pors=pors, result=result, projects=projects, work=work, skills=skills)
    options = {
        'page-size': 'TABLOID',  # Set the page size to A4
        'margin-top': '0cm',  # Set the top margin to 1cm
        'margin-bottom': '0cm',  # Set the bottom margin to 1cm
        'margin-left': '0cm',  # Set the left margin to 1cm
        'margin-right': '0cm',  # Set the right margin to 1cm
        "enable-local-file-access": "",
        'encoding': "UTF-8",  # Specify the encoding
    }
    os.environ['LD_LIBRARY_PATH'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
    path_wkhtmltopdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bin', 'wkhtmltopdf')
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(htmlFile, False, options=options, configuration=config)

    # Return the PDF as a file
    return send_file(BytesIO(pdf), mimetype='application/pdf', as_attachment=True, download_name='resume.pdf')


@app.route('/resume-view', methods=['GET'])
def resume_view():
    about_me_data=AboutMe.query.first()
    education_data = Education.query.all()
    pors=POR.query.all()
    result=Result.query.all()
    projects=Project.query.all()
    work=Work.query.all()
    skills=Skill.query.all()
    return render_template('resume.html', about_me_data=about_me_data, education_data=education_data, pors=pors, result=result, projects=projects, work=work, skills=skills)



@app.route('/delete/<string:table_name>/<int:id>', methods=['POST'])
def delete_item(table_name, id):
    if table_name == 'about_me':
        item = AboutMe.query.get_or_404(id)
    elif table_name == 'education':
        item = Education.query.get_or_404(id)
    elif table_name == 'por':
        item = POR.query.get_or_404(id)
    elif table_name == 'result':
        item = Result.query.get_or_404(id)
    elif table_name == 'projects':
        item = Project.query.get_or_404(id)
    elif table_name == 'work':
        item = Work.query.get_or_404(id)
    elif table_name == 'skills':
        item = Skill.query.get_or_404(id)
    else:
        flash('Invalid table name')
        return redirect(url_for('edit_page'))

    if item:  # Check if item is not None
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('edit_page'))
    else:
        flash('Item not found')
        return redirect(url_for('edit_page'))


class AboutMe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paragraph = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(100), nullable=True)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(100), nullable=True)
    institution = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(100), nullable=True)

class POR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.String(100), nullable=True)
    image_url = db.Column(db.String(100), nullable=True)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    Score = db.Column(db.String(100), nullable=True)
    institution = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(100), nullable=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    github_repo = db.Column(db.String(200), nullable=True)
    image_url = db.Column(db.String(100), nullable=True)

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(100), nullable=True)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=True)
    date = db.Column(db.String(100), nullable=True)
    link = db.Column(db.String(200), nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(100), nullable=True)

def update_ids(table):
    def update_ids_func(mapper, connection, target):
        session = sessionmaker(bind=connection)()
        max_id = session.query(table.id).order_by(table.id.desc()).first()
        if max_id is not None:
            session.query(table).filter(table.id > target.id).update({table.id: table.id - 1}, synchronize_session=False)
        session.commit()
    event.listen(table, 'after_delete', update_ids_func)

# Apply the trigger function to each table
update_ids(AboutMe)
update_ids(Education)
update_ids(POR)
update_ids(Result)
update_ids(Project)
update_ids(Work)
update_ids(Skill)

if __name__=='__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
