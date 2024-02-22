from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class LibroForm(FlaskForm):
    titulo = StringField('Título del Libro', validators=[DataRequired(), Length(max=100)])
    autor = StringField('Autor del Libro', validators=[DataRequired(), Length(max=100)])
    genero = StringField('Género del Libro', validators=[DataRequired(), Length(max=50)])
    anio_publicacion = IntegerField('Año de Publicación', validators=[DataRequired()])
    editorial = StringField('Editorial', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Registrar Libro')