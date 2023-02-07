namespace AspFilesLoadApp
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);
            var app = builder.Build();

            app.Run(async (context) => {
                var response = context.Response;
                var request = context.Request;

                response.ContentType = "text/html; charset=utf-8";

                if (request.Path == "/upload" && request.Method == "POST")
                {
                    var files = request.Form.Files;
                    var pathUpload = $"{Directory.GetCurrentDirectory()}/upload";
                    Directory.CreateDirectory(pathUpload);

                    foreach (var file in files)
                    {
                        string pathFile = $"{pathUpload}/{file.FileName}";
                        using (var fileStream = File.OpenWrite(pathFile))
                        {
                            await file.CopyToAsync(fileStream);
                        }
                    }
                    await response.WriteAsync("File uploades");
                }
                else
                    await response.SendFileAsync("html/index.html");

            });

            

            
            app.Run();
        }
    }
}