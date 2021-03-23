from django.contrib import admin


from .models import User, Genres, Categories, Titles, Review, Comment


class UserAdmin(admin.ModelAdmin):
    pass


class GenresAdmin(admin.ModelAdmin):
    pass


class CategoriesAdmin(admin.ModelAdmin):
    pass


class TitlesAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Titles, TitlesAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
